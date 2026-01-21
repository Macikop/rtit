#!/usr/bin/env python3

import mariadb
import random
import datetime
import sys

import db_lib

names = [
    "Jan", "Anna", "Piotr", "Maria", "Krzysztof", "Magdalena", "Tomasz", "Agnieszka", "Paweł", "Katarzyna",
    "Michał", "Joanna", "Mateusz", "Ewa", "Marcin", "Aleksandra", "Łukasz", "Monika", "Adam", "Natalia"
]

surnames = [
    "Kowalski", "Nowak", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamińska", "Lewandowski", "Zielińska", "Szymański", "Woźniak",
    "Dąbrowski", "Kozłowska", "Jankowski", "Mazur", "Kwiatkowska", "Wojciechowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowska"
]

nicknames_first = [
    "Jeziorny",
    "Wodny",
    "Błękitny",
    "Leśny",
    "Słoneczny",
    "Cichy",
    "Złoty",
    "Mroczny",
    "Tęczowy",
    "Mglisty",
    "Zielony",
    "Kamienny",
    "Srebrny",
    "Wietrzny",
    "Piaskowy",
    "Szumiący",
    "Skryty",
    "Błotny",
    "Krystaliczny",
    "Dziki"
]

nicknames_second = [
    "Żeglarz",
    "Wędrowiec",
    "Rybak",
    "Pływak",
    "Brzeg",
    "Fale",
    "Szczupak",
    "Głębina",
    "Karp",
    "Poranek",
    "Sitowie",
    "Pomost",
    "Okoń",
    "Zatoka",
    "Trzciny",
    "Żuraw",
    "Wodnik",
    "Łabędź",
    "Mewa",
    "Perkoz"
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

def random_date(start_year = 2010, end_year = 2020):
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    delta = end - start
    return start + datetime.timedelta(days = random.randint(0, delta.days))


def connect_and_insert_random(people_number = 1, turnus = 1):
     
    print("This function isn't acctive, try generating random list and loading it")
    #conn, cursor = connect_to_db()
    #try:
    #    cursor.execute("DELETE FROM uczestnik")
    #
    #    for id in range(people_number):
    #        imie = random.choice(names)
    #        nazwisko = random.choice(surnames)
    #        dataUrodzenia = random_date()
    #        plec = random.choice(["Mężczyzna", "Kobieta"])
    #        pierwszyRaz = random.choice(["tak", "nie"])
    #        leki = random.choice(["tak", "nie"])
    #
    #        cursor.execute(
    #                "INSERT INTO uczestnik (id, imie, nazwisko, dataUrodzenia, plec, turnus, pierwszyRaz, Leki) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    #                (id, imie, nazwisko, dataUrodzenia, plec, turnus, pierwszyRaz, leki)
    #            )
    #        
    #    cursor.execute("SELECT id FROM uczestnik WHERE pierwszyRaz = 'tak'")
    #    ids = [row[0] for row in cursor.fetchall()]
    #    for new_child_id in ids:
    #         cursor.execute("UPDATE uczestnik SET imieObozowe = ? WHERE id = ?", (random.choice(nicknames_first) + ' ' +  random.choice(nicknames_second), new_child_id))
    #    
    #except mariadb.Error as e:
    #    print(f"Error: {e}")
    #
    #conn.commit()
    #cursor.close()
    #conn.close()

def insert_random_nicknames():
    conn, cursor = connect_to_db()
    try:
        cursor.execute("SELECT id FROM uczestnik WHERE pierwszyRaz = 'tak'")
        ids = [row[0] for row in cursor.fetchall()]
        for new_child_id in ids:
             cursor.execute("UPDATE uczestnik SET imieObozowe = ? WHERE id = ?", (random.choice(nicknames_first) + ' ' +  random.choice(nicknames_second), new_child_id))
        
    except mariadb.Error as e:
        print(f"Error: {e}")

    conn.commit()
    cursor.close()
    conn.close()

def insert_and_link_runmagedon(skip_category=False, show_summary=True):
    """Create or update runmagedon records for participants.

    If skip_category is True, existing kategoria values are preserved and no new random categories
    are assigned. Otherwise, participants without an existing category receive a random one.
    Times (czasStartu, czasMety, wynik) are always (re)generated.
    """
    conn, cursor = connect_to_db()

    categories = ["Grupa1", "Grupa2", "Grupa3"]

    # Operate on all participants; we'll insert or update runmagedon rows as needed
    cursor.execute("SELECT id FROM uczestnik ORDER BY id;")
    participants = [row[0] for row in cursor.fetchall()]

    if not participants:
        print("⚠️ No participants available to process.")
        return

    start_time = datetime.datetime.combine(datetime.date.today(), datetime.time(0, 0, 0))
    step = datetime.timedelta(seconds=30)

    summary = []

    for i, uczestnik_id in enumerate(participants):
        # Check existing runmagedon row and category
        cursor.execute("SELECT kategoria FROM runmagedon WHERE id = %s", (uczestnik_id,))
        row = cursor.fetchone()
        if row:
            existing_cat = row[0]
        else:
            existing_cat = None

        if skip_category:
            kategoria = existing_cat  # preserve whatever was set (may be None)
        else:
            # if existing category present, keep it; otherwise assign random
            kategoria = existing_cat if existing_cat else random.choice(categories)

        # --- Generate times ---
        current_start = start_time + i * step
        duration = datetime.timedelta(minutes=random.randint(5, 30), seconds=random.randint(0, 59))
        current_finish = current_start + duration

        # --- Compute wynik = czasMety - czasStartu ---
        wynik_timedelta = current_finish - current_start
        wynik = str(wynik_timedelta).split(".")[0]  # format HH:MM:SS

        # --- upsert into runmagedon with the same ID as uczestnik ---
        if row:
            cursor.execute("UPDATE runmagedon SET wynik = %s, kategoria = %s, czasStartu = %s, czasMety = %s WHERE id = %s",
                           (wynik, kategoria, current_start.time(), current_finish.time(), uczestnik_id))
        else:
            cursor.execute("INSERT INTO runmagedon (id, wynik, kategoria, czasStartu, czasMety) VALUES (%s, %s, %s, %s, %s)",
                           (uczestnik_id, wynik, kategoria, current_start.time(), current_finish.time()))

        # --- link uczestnik to runmagedon ---
        cursor.execute("UPDATE uczestnik SET runmagedon = %s WHERE id = %s", (uczestnik_id, uczestnik_id))

        summary.append((uczestnik_id, wynik, kategoria, current_start.time(), current_finish.time()))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ Processed and linked {len(participants)} runmagedon results (IDs matched).")
    if show_summary:
        print("\nSummary:")
        for uid, wynik, cat, start, stop in summary:
            print(f"  ID {uid:3} | wynik: {wynik:8} | kategoria: {cat or 'NULL':8} | start: {start} | meta: {stop}")

def cleanup_runmagedon():

    conn, cursor = connect_to_db()
        # Disable foreign key checks temporarily to avoid constraint errors
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

    # Step 1: Unlink all uczestnik entries
    cursor.execute("UPDATE uczestnik SET runmagedon = NULL;")

    # Step 2: Delete all runmagedon entries
    cursor.execute("DELETE FROM runmagedon;")

    # Re-enable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

    conn.commit()
    cursor.close()
    conn.close()
    print("🧹 All runmagedon records deleted and uczestnik links cleared.")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        match args[1]:
            case '-h' | '--help':
                print("Randomiser - inserts random data to db\n -r - add random records to db\n -f - fill nicknames to eligible people\n -t - fill turnamen with random times (right now runmagedon)\n -tc fill turnament without category")
            case '-r':
                if len(args) == 3:
                    try:
                        record_number = int(args[2])
                        connect_and_insert_random(record_number)
                        print("Data inserted")
                    except:
                        print("Second argument must be an integer")
                else:
                    if len(args) < 3:
                        print("Too few arguments")
                    else:
                        print("Too many arguments")
            case '-f':
                insert_random_nicknames()
                print("Random nicknames added")
            case '-t':
                # Fill times only, preserve existing categories
                insert_and_link_runmagedon(skip_category=True)
                print("Runmagedon times filled (categories preserved)")
            case '-tc':
                # Fill times only, also do not assign new categories
                insert_and_link_runmagedon(True)
                print("Runmagedon times filled (categories preserved)")
            case _:
                print("Unknown option, use -h or --help") 
    else:
        print("Randomiser: use -h or --help")