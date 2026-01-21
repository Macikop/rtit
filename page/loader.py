#!/usr/bin/env python3
 
import mariadb
import csv
import os
import sys
import random

from functools import partial
from unicodedata import normalize

import db_lib

WYCHOWAWCY = [
    ("Jan", "Kowalski"),
    ("Anna", "Nowak"),
    ("Piotr", "Wiśniewski"),
    ("Maria", "Zielińska"),
    ("Tomasz", "Kaczmarek"),
    ("Katarzyna", "Mazur"),
    ("Michał", "Lewandowski"),
    ("Agnieszka", "Dąbrowska"),
    ("Paweł", "Wójcik"),
    ("Monika", "Kamińska"),
]


def connect_to_db():
    login = db_lib.get_db_data()
    try: 
        conn = mariadb.connect(user = login['user'],
                            password = login['password'],
                            host = login['host'],
                            database = login['database'])
        
        cur = conn.cursor()
        return conn, cur 
    except mariadb.Error as e:
        print("Connection error:", e)
        return None, None
    
def read_csv_file(path):
    with open(path, "r", newline='') as csvfile:
        return csv.reader(csvfile, delimiter=',',  quotechar='|')
    
def import_to_db(filename, turnus):
    conn, cur = connect_to_db()

    # Reset related tables to ensure a clean load
    try:
        cur.execute("SET SESSION FOREIGN_KEY_CHECKS=0;")
    except mariadb.Error as e:
        print("Warning: couldn't disable foreign key checks:", e)

    tables = ["wychowawca", "runmagedon", "biegi", "plywanie", "uczestnik"]
    for t in tables:
        try:
            cur.execute(f"TRUNCATE TABLE {t}")
        except mariadb.Error:
            # FALLBACK: delete rows and reset AUTO_INCREMENT
            try:
                cur.execute(f"DELETE FROM {t}")
                cur.execute(f"ALTER TABLE {t} AUTO_INCREMENT = 1")
            except mariadb.Error as e:
                print(f"Warning: couldn't clear table {t}:", e)

    try:
        cur.execute("SET SESSION_FOREIGN_KEY_CHECKS=1;")
    except mariadb.Error as e:
        # try the correct command if the above failed
        try:
            cur.execute("SET SESSION FOREIGN_KEY_CHECKS=1;")
        except mariadb.Error as e2:
            print("Warning: couldn't re-enable foreign key checks:", e2)

    conn.commit()

    turnus_list = []
    with open(os.path.join(os.path.dirname(__file__), filename), "r", newline='') as csvfile:
        for row in csv.reader(csvfile, delimiter=',',  quotechar='|'):
            for i, filed in enumerate(row):
                row[i] = filed.replace('"', '')
            try:
                child_turnus = int(row[3])
                if child_turnus == turnus:
                    turnus_list.append(row)
            except:
                pass
    
    norm = partial(normalize, 'NFD')
    turnus_list = sorted(turnus_list, key=lambda row: (norm(row[2]), norm(row[1])))
    #print(turnus_list)
        
    for id, child in enumerate(turnus_list):
        cur.execute(
                    "INSERT INTO uczestnik (id, imie, nazwisko, dataUrodzenia, plec, turnus, pierwszyRaz, leki) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (id, child[1], child[2], child[4], child[6], child[3] ,child[5], child[7])
                )
 
    conn.commit()
    cur.close()        
    conn.close()



def assign_wychowawcy(wychowawcy):
    """
    Assigns a random wychowawca to each participant.
    wychowawcy: list of tuples [(imie, nazwisko), ...]
    """
    conn, cur = connect_to_db()

    # Try to disable foreign key checks for this session so malformed FK constraints won't block inserting wychowawcy
    try:
        cur.execute("SET SESSION FOREIGN_KEY_CHECKS=0;")
    except mariadb.Error as e:
        print("Warning: couldn't disable foreign key checks:", e)

    try:
        # Clear wychowawca table
        cur.execute("DELETE FROM wychowawca")

        # Ensure wychowawca.id is AUTO_INCREMENT (fix for 'Field id doesn't have a default value')
        try:
            cur.execute("ALTER TABLE wychowawca MODIFY COLUMN id INT NOT NULL AUTO_INCREMENT;")
        except mariadb.Error:
            try:
                cur.execute("ALTER TABLE wychowawca ADD COLUMN id INT NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST;")
            except mariadb.Error as e:
                print("Warning: couldn't make wychowawca.id AUTO_INCREMENT:", e)

        # Insert wychowawcy (include default 'wolne' for zajecia to avoid NOT NULL errors)
        try:
            wychowawcy_with_zaj = [(im, naz, 'wolne') for (im, naz) in wychowawcy]
            cur.executemany(
                "INSERT INTO wychowawca (imie, nazwisko, zajecia) VALUES (?, ?, ?)",
                wychowawcy_with_zaj
            )
        except mariadb.IntegrityError as e:
            # Likely: Field 'id' doesn't have a default value and user lacks ALTER privileges
            print("IntegrityError inserting wychowawcy (fallback to explicit ids):", e)
            cur.execute("SELECT MAX(id) FROM wychowawca")
            max_row = cur.fetchone()
            start_id = (max_row[0] or 0) + 1
            wychowawcy_with_id = [(start_id + i, im, naz, 'wolne') for i, (im, naz) in enumerate(wychowawcy)]
            cur.executemany(
                "INSERT INTO wychowawca (id, imie, nazwisko, zajecia) VALUES (?, ?, ?, ?)",
                wychowawcy_with_id
            )
        except mariadb.Error as e:
            # Any other DB error during insert -> try explicit ids as a fallback
            print("Error inserting wychowawcy, attempting fallback with explicit ids:", e)
            cur.execute("SELECT MAX(id) FROM wychowawca")
            max_row = cur.fetchone()
            start_id = (max_row[0] or 0) + 1
            wychowawcy_with_id = [(start_id + i, im, naz, 'wolne') for i, (im, naz) in enumerate(wychowawcy)]
            cur.executemany(
                "INSERT INTO wychowawca (id, imie, nazwisko, zajecia) VALUES (?, ?, ?, ?)",
                wychowawcy_with_id
            )

        # Ensure zajecia default is applied for any existing rows (NULL or empty)
        try:
            cur.execute("UPDATE wychowawca SET zajecia = 'wolne' WHERE zajecia IS NULL OR zajecia = ''")
        except mariadb.Error as e:
            print("Warning: couldn't set default zajecia:", e)

        # Get wychowawca IDs
        cur.execute("SELECT id FROM wychowawca")
        wychowawca_ids = [row[0] for row in cur.fetchall()]

    finally:
        # Ensure FK checks are re-enabled for this session
        try:
            cur.execute("SET SESSION FOREIGN_KEY_CHECKS=1;")
        except mariadb.Error as e:
            print("Warning: couldn't re-enable foreign key checks:", e)

    # Get wychowawca IDs
    cur.execute("SELECT id FROM wychowawca")
    wychowawca_ids = [row[0] for row in cur.fetchall()]

    if not wychowawca_ids:
        print("No wychowawcy available")
        return

    # Get all participant IDs
    cur.execute("SELECT id FROM uczestnik")
    uczestnicy = [row[0] for row in cur.fetchall()]

    # Randomize order
    random.shuffle(uczestnicy)

    # Assign random wychowawca to each participant
    for uczestnik_id in uczestnicy:
        cur.execute(
            "UPDATE uczestnik SET wychowawca = ? WHERE id = ?",
            (random.choice(wychowawca_ids), uczestnik_id)
        )

    conn.commit()
    cur.close()
    conn.close()

    print("✔ Random wychowawca assigned to each participant")

    


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        match args[1]:
            case '-h' | '--help':
                print("Loader - loads form to db. Use -l to load form to db")
            case '-l':
                if len(args) == 3:
                    try:
                        turnus = int(args[2])
                        import_to_db("loader/uczestnicy.csv", turnus)
                        assign_wychowawcy(WYCHOWAWCY)
                        print("Data inserted and wychowawcy assigned")
                    except ValueError:
                        print("Second argument must be an integer")
                else:
                    print("Usage: script.py -l <turnus>")
    else:
        print("Randomiser: use -h or --help")