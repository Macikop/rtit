from flask import Flask, render_template_string, url_for, send_file, request, redirect
import os
import subprocess
import sys
import mariadb
import db_lib
import datetime
import calendar

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Rusz Tyłek</title>
    <style>
        body {
            font-family: "Times New Roman", serif;
            margin: 30px;
            color: black;
            background-color: white;
        }

        h1 {
            font-size: 32px;
            margin-bottom: 10px;
        }

        p {
            font-size: 16px;
            margin-bottom: 20px;
        }

        .menu {
            display: flex;
            flex-direction: column;
            gap: 6px;
            width: fit-content;
        }

        .btn-link {
            display: inline-block;
            font-family: Arial, sans-serif;
            font-size: 14px;
            padding: 2px 8px;
            border: 1px solid gray;
            background-color: #f0f0f0;
            color: black;
            text-decoration: none;
        }

        .btn-link:hover {
            background-color: #e0e0e0;
        }

        .btn-link:active {
            background-color: #d0d0d0;
        }
    </style>
</head>
<body>

<h1>Witamy w interfejsie Rusz Tyłek</h1>

<p>Ten interfejs umożliwia zarządzanie ludźmi na RT.</p>

<div class="menu">
    <a class="btn-link" href="{{ url_for('grupa_wychowawcy') }}">Grupa wychowawcy</a>
    <a class="btn-link" href="{{ url_for('grupy_innych') }}">Grupy innych</a>
    <a class="btn-link" href="{{ url_for('urodziny') }}">Info o urodzinach</a>
    <a class="btn-link" href="{{ url_for('kategorie') }}">tworzenie kategorii, wybranie roczników i płci</a>
    <a class="btn-link" href="{{ url_for('zawody') }}">wpisywanie zawodów, razem z generowaniem zawodów</a>
    <a class="btn-link" href="{{ url_for('legitymacje') }}">Generator Legitymacji</a>
    <a class="btn-link" href="{{ url_for('zajecia') }}">Zajęcia</a>
</div>

{{ top_link|safe }}

<!--TURNUS_TABLE-->

</body>
</html>
"""

@app.route("/")
def index():
    # Determine current Turnus and display it as a single text line
    today = datetime.date.today()
    try:
        login = db_lib.get_db_data()
        conn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT turnus FROM uczestnik")
        rows = [r[0] for r in cur.fetchall()]

        # Get today's birthdays (order by participant id)
        cur.execute("SELECT imie, nazwisko FROM uczestnik WHERE dataUrodzenia IS NOT NULL AND MONTH(dataUrodzenia) = ? AND DAY(dataUrodzenia) = ? ORDER BY id", (today.month, today.day))
        birthday_rows = cur.fetchall()

        # Get current wychowawca info for id=1 and participants in their zajecia
        try:
            cur.execute("SELECT imie, nazwisko, zajecia FROM wychowawca WHERE id = ?", (1,))
            row = cur.fetchone()
            if row:
                wych_name = f"{row[0]} {row[1]}"
                wych_zaj = row[2] if row[2] else ''
                # find participants who have the same zajecia (empty string means wolne)
                if wych_zaj != '':
                    cur.execute("SELECT u.id, u.imie, u.nazwisko FROM uczestnik u LEFT JOIN wychowawca w ON u.wychowawca = w.id WHERE COALESCE(w.zajecia, '') = ? ORDER BY u.id", (wych_zaj,))
                else:
                    cur.execute("SELECT id, imie, nazwisko FROM uczestnik WHERE id IN (SELECT u.id FROM uczestnik u LEFT JOIN wychowawca w ON u.wychowawca = w.id WHERE COALESCE(w.zajecia, '') = '') ORDER BY id")
                wych_participants = cur.fetchall()
            else:
                wych_name = 'Wychowawca 1'
                wych_zaj = ''
                wych_participants = []
        except mariadb.Error:
            wych_name = 'Wychowawca 1'
            wych_zaj = ''
            wych_participants = []

        cur.close()
        conn.close()
    except mariadb.Error:
        rows = []
        birthday_rows = []
        wychowawcy = []

    if not rows:
        turnus_html = '<p>Aktualny turnus: brak danych</p>'
    elif len(rows) == 1:
        turnus_html = f'<p>Aktualny turnus: {rows[0]}</p>'
    else:
        turnus_html = f'<p>Aktualny turnus: różne ({", ".join(str(x) for x in rows)})</p>'

    # Build today's birthday line
    if birthday_rows:
        names = [f"{r[0]} {r[1]}" for r in birthday_rows]
        birthday_html = f'<p><strong>Dzisiaj mają urodziny:</strong> {", ".join(names)}</p>'
    else:
        birthday_html = '<p>Dzisiaj nie ma urodzin.</p>'

    # Get current wychowawca info (prefer id=1, otherwise fall back to first wychowawca row)
    # Use previously fetched 'row' and 'wych_participants' if available; avoid re-using a closed cursor.
    if 'row' in locals() and row:
        # we already fetched a row and possibly wych_participants above
        pass
    else:
        try:
            login = db_lib.get_db_data()
            conn2 = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
            cur2 = conn2.cursor()
            cur2.execute("SELECT imie, nazwisko, zajecia FROM wychowawca WHERE id = ?", (1,))
            row = cur2.fetchone()
            if not row:
                cur2.execute("SELECT imie, nazwisko, zajecia FROM wychowawca ORDER BY id LIMIT 1")
                row = cur2.fetchone()
            cur2.close()
            conn2.close()
        except mariadb.Error:
            row = None

    if row:
        wych_name = f"{row[0]} {row[1]}"
        wych_zaj = row[2] if row[2] else ''
    else:
        wych_name = 'Wychowawca 1'
        wych_zaj = ''

    # Build compact wychowawca info for main page (no table)
    wych_info = f'<p><strong>Wychowawca:</strong> {wych_name}</p><p><strong>Zajęcia:</strong> {wych_zaj if wych_zaj else "wolne"}</p>'

    # No back-to-main on index page
    return render_template_string(HTML.replace('<!--TURNUS_TABLE-->', wych_info + turnus_html + birthday_html), top_link='')

@app.route("/grupa-wychowawcy", methods=["GET", "POST"])
def grupa_wychowawcy():
    """
    Show participants assigned to wychowawca id 1 and display wychowawca name on top.
    For those with "pierwszyRaz" == 'tak', allow editing `imieObozowe` and submit changes to DB.
    """
    wych_id = 1

    msg = None

    # Handle form submission
    if request.method == 'POST':
        # Collect fields of form named obozowe_<id>
        updates = []
        for key, val in request.form.items():
            if not key.startswith('obozowe_'):
                continue
            try:
                pid = int(key.split('_', 1)[1])
            except Exception:
                continue
            imie_obozowe = val.strip() or None
            updates.append((imie_obozowe, pid))

        if updates:
            try:
                login = db_lib.get_db_data()
                conn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
                cur = conn.cursor()
                # Only update imieObozowe for participants who have pierwszyRaz = 'tak'
                for imie_obozowe, pid in updates:
                    cur.execute("UPDATE uczestnik SET imieObozowe = ? WHERE id = ? AND pierwszyRaz = 'tak'", (imie_obozowe, pid))
                conn.commit()
                cur.close()
                conn.close()
                msg = 'Zapisano zmiany.'
            except mariadb.Error as e:
                msg = f'Błąd zapisu: {e}'

    # Connect to DB to fetch data for display
    try:
        login = db_lib.get_db_data()
        conn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
        cur = conn.cursor()
    except mariadb.Error as e:
        return f"DB connection error: {e}", 500

    try:
        # Get wychowawca name
        cur.execute("SELECT imie, nazwisko FROM wychowawca WHERE id = ?", (wych_id,))
        row = cur.fetchone()
        wych_name = f"{row[0]} {row[1]}" if row else f"Wychowawca {wych_id}"

        # Get participants assigned to that wychowawca (ordered by id)
        cur.execute("""SELECT id, imie, nazwisko, dataUrodzenia, plec, pierwszyRaz, leki, imieObozowe
                       FROM uczestnik WHERE wychowawca = ? ORDER BY id""", (wych_id,))
        uczestnicy = cur.fetchall()
    except mariadb.Error as e:
        cur.close()
        conn.close()
        return f"DB query error: {e}", 500
    finally:
        cur.close()
        conn.close()

    template = """
    <!doctype html>
    <html lang="pl">
    <head>
      <meta charset="utf-8">
      <title>Grupa wychowawcy</title>
      <style>input.text {width: 100%; box-sizing: border-box}</style>
    </head>
    <body>
      {{ top_link|safe }}
      <h1>Grupa wychowawcy: {{ wych_name }}</h1>
      {% if msg %}
        <p><strong>{{ msg }}</strong></p>
      {% endif %}
      {% if uczestnicy %}
      <form method="post">
      <table border="1" cellpadding="6" cellspacing="0">
        <thead>
          <tr>
            <th>Lp.</th>
            <th>Imię</th>
            <th>Nazwisko</th>
            <th>Data urodzenia</th>
            <th>Płeć</th>
            <th>Pierwszy raz</th>
            <th>Leki</th>
            <th>Imię obozowe</th>
          </tr>
        </thead>
        <tbody>
        {% for u in uczestnicy %}
          <tr>
            <td>{{ loop.index }}</td>
            <td>{{ u[1] }}</td>
            <td>{{ u[2] }}</td>
            <td>{{ u[3] }}</td>
            <td>{{ u[4] }}</td>
            <td>{{ u[5] }}</td>
            <td>{{ u[6] }}</td>
            <td>
              {% if u[5] == 'tak' %}
                <input class="text" name="obozowe_{{ u[0] }}" value="{{ u[7] or '' }}">
              {% else %}
                {{ u[7] or '' }}
              {% endif %}
            </td>
          </tr>
        {% endfor %}
        </tbody>
      </table>
      <p><button type="submit">Zapisz imiona obozowe</button></p>
      </form>
      {% else %}
      <p>Brak uczestników przypisanych do tego wychowawcy.</p>
      {% endif %}
    </body>
    </html>
    """

    top_link = f'<a class="btn-link" href="{url_for("index")}">Powrót do strony głównej</a>'
    return render_template_string(template, wych_name=wych_name, uczestnicy=uczestnicy, msg=msg, top_link=top_link)

@app.route("/grupy-innych")
def grupy_innych():
    """
    Show participants grouped by each wychowawca except id 1, plus an "Unassigned" group.
    """
    exclude_id = 1

    # Connect to DB
    try:
        login = db_lib.get_db_data()
        conn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
        cur = conn.cursor()
    except mariadb.Error as e:
        return f"DB connection error: {e}", 500

    groups = []
    try:
        # Get all wychowawcy except the excluded one
        cur.execute("SELECT id, imie, nazwisko FROM wychowawca WHERE id != ? ORDER BY nazwisko, imie", (exclude_id,))
        wychowawcy = cur.fetchall()

        for wych in wychowawcy:
            wid, im, naz = wych
            cur.execute("""SELECT id, imie, nazwisko, dataUrodzenia, plec, pierwszyRaz, leki, turnus
                           FROM uczestnik WHERE wychowawca = ? ORDER BY id""", (wid,))
            uczestnicy = cur.fetchall()
            groups.append({'name': f"{im} {naz}", 'uczestnicy': uczestnicy})

        # Add an 'Unassigned' group (wychowawca IS NULL)
        cur.execute("""SELECT id, imie, nazwisko, dataUrodzenia, plec, pierwszyRaz, leki, turnus
                       FROM uczestnik WHERE wychowawca IS NULL ORDER BY id""")
        unassigned = cur.fetchall()
        groups.append({'name': 'Bez wychowawcy', 'uczestnicy': unassigned})

    except mariadb.Error as e:
        cur.close()
        conn.close()
        return f"DB query error: {e}", 500
    finally:
        cur.close()
        conn.close()

    template = """
    <!doctype html>
    <html lang="pl">
    <head>
      <meta charset="utf-8">
      <title>Grupy innych wychowawców</title>
      <style>table{border-collapse:collapse;} th, td{padding:6px 8px; border:1px solid #ccc;}</style>
    </head>
    <body>
      {{ top_link|safe }}
      <h1>Grupy innych wychowawców</h1>
      {% for g in groups %}
        <h2>{{ g.name }}</h2>
        {% if g.uczestnicy %}
        <table>
          <thead>
            <tr>
              <th>Lp.</th>
              <th>Imię</th>
              <th>Nazwisko</th>
              <th>Data urodzenia</th>
              <th>Płeć</th>
              <th>Pierwszy raz</th>
              <th>Leki</th>
            </tr>
          </thead>
          <tbody>
          {% for u in g.uczestnicy %}
            <tr>
              <td>{{ loop.index }}</td>
              <td>{{ u[1] }}</td>
              <td>{{ u[2] }}</td>
              <td>{{ u[3] }}</td>
              <td>{{ u[4] }}</td>
              <td>{{ u[5] }}</td>
              <td>{{ u[6] }}</td>
            </tr>
          {% endfor %}
          </tbody>
        </table>
        {% else %}
          <p>Brak uczestników w tej grupie.</p>
        {% endif %}
        <hr/>
      {% endfor %}
    </body>
    </html>
    """

    top_link = f'<a class="btn-link" href="{url_for("index")}">Powrót do strony głównej</a>'
    return render_template_string(template, groups=groups, top_link=top_link)

@app.route("/urodziny")
def urodziny():
    """
    Render a calendar for the current month and list names of participants
    who have birthdays on each day. Highlight today's date in green when applicable.
    """
    today = datetime.date.today()
    year = today.year
    month = today.month

    # Polish month names
    month_names = ["", "Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
    month_name = month_names[month]

    # Fetch birthdays in the current month
    try:
        login = db_lib.get_db_data()
        conn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
        cur = conn.cursor()
        cur.execute("SELECT imie, nazwisko, dataUrodzenia FROM uczestnik WHERE dataUrodzenia IS NOT NULL AND MONTH(dataUrodzenia) = ? ORDER BY DAY(dataUrodzenia), id", (month,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except mariadb.Error as e:
        return f"DB error: {e}", 500

    births = {}
    for imie, nazwisko, data in rows:
        if not data:
            continue
        # data is a date object
        day = data.day if hasattr(data, 'day') else int(str(data).split('-')[2])
        births.setdefault(day, []).append(f"{imie} {nazwisko}")

    # Calendar layout (weeks starting on Monday)
    cal = calendar.monthcalendar(year, month)
    weekdays = ['Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'So', 'Nd']

    highlight_day = today.day if (today.month == month and today.year == year) else 0

    template = """
    <!doctype html>
    <html lang="pl">
    <head>
      <meta charset="utf-8">
      <title>Urodziny - {{ month_name }} {{ year }}</title>
      <style>
        table.calendar { border-collapse: collapse; width: 100%; }
        table.calendar th, table.calendar td { border: 1px solid #ccc; vertical-align: top; padding: 6px; width: 14.28%; height: 120px; }
        table.calendar th { background: #f5f5f5; }
        .daynum { font-weight: bold; margin-bottom: 6px; }
        .today { background-color: #c6f6c6; }
        .names { font-size: 0.95em; }
      </style>
    </head>
    <body>
      {{ top_link|safe }}
      <h1>Urodziny — {{ month_name }} {{ year }}</h1>
      <table class="calendar">
        <thead>
          <tr>
            {% for wd in weekdays %}
            <th>{{ wd }}</th>
            {% endfor %}
          </tr>
        </thead>
        <tbody>
          {% for week in cal %}
          <tr>
            {% for d in week %}
              {% if d == 0 %}
                <td></td>
              {% else %}
                <td class="{% if d == highlight_day %}today{% endif %}">
                  <div class="daynum">{{ d }}</div>
                  <div class="names">
                    {% for name in births.get(d, []) %}
                      <div>{{ name }}</div>
                    {% endfor %}
                  </div>
                </td>
              {% endif %}
            {% endfor %}
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </body>
    </html>
    """

    return render_template_string(template, year=year, cal=cal, weekdays=weekdays, births=births, highlight_day=highlight_day, month_name=month_name)

@app.route("/kategorie", methods=["GET", "POST"])
def kategorie():
    """Create and save categories based on gender and birth year range.

    Preview shows how many participants match. Save will set/insert
    `runmagedon.kategoria` for matching participants and link them (id).
    """
    top_link = f'<a class="btn-link" href="{url_for("index")}">Powrót do strony głównej</a>'

    msg = None
    preview_count = None
    preview_sample = []
    matched_list = None

    # Determine year bounds from DB
    try:
        login = db_lib.get_db_data()
        conn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
        cur = conn.cursor()
        cur.execute("SELECT MIN(YEAR(dataUrodzenia)), MAX(YEAR(dataUrodzenia)) FROM uczestnik WHERE dataUrodzenia IS NOT NULL")
        min_max = cur.fetchone()
        min_year = min_max[0] or datetime.date.today().year
        max_year = min_max[1] or datetime.date.today().year
    except mariadb.Error as e:
        return f"DB connection error: {e}", 500

    # Handle form submission
    selected_gender = 'ALL'
    selected_start_year = min_year
    selected_end_year = max_year
    selected_contest = 'runmagedon'

    if request.method == 'POST':
        selected_gender = request.form.get('gender', 'ALL')  # 'M', 'K', 'ALL'
        selected_contest = request.form.get('contest', 'runmagedon')
        gender = selected_gender
        try:
            start_year = int(request.form.get('start_year', min_year))
            end_year = int(request.form.get('end_year', max_year))
            selected_start_year = start_year
            selected_end_year = end_year
        except ValueError:
            msg = 'Roczniki muszą być liczbami.'
            # Keep submitted values if present
            ssy = request.form.get('start_year', '')
            sey = request.form.get('end_year', '')
            try:
                selected_start_year = int(ssy)
            except Exception:
                selected_start_year = min_year
            try:
                selected_end_year = int(sey)
            except Exception:
                selected_end_year = max_year
            cur.close(); conn.close()
            return render_template_string(KATEGORIE_TEMPLATE, top_link=top_link, msg=msg, preview_count=preview_count, preview_sample=preview_sample, matched_list=matched_list, min_year=min_year, max_year=max_year, selected_gender=selected_gender, selected_start_year=selected_start_year, selected_end_year=selected_end_year, selected_contest=selected_contest)

        if start_year > end_year:
            msg = 'Rok początkowy nie może być większy niż końcowy.'
        else:
            # Build query
            sql = "SELECT id, imie, nazwisko, YEAR(dataUrodzenia) FROM uczestnik WHERE dataUrodzenia IS NOT NULL AND YEAR(dataUrodzenia) BETWEEN ? AND ?"
            params = [start_year, end_year]
            if gender == 'M':
                sql += " AND plec = ?"
                params.append('Mężczyzna')
            elif gender == 'K':
                sql += " AND plec = ?"
                params.append('Kobieta')

            try:
                cur.execute(sql + ' ORDER BY id', params)
                matched = cur.fetchall()
                preview_count = len(matched)
                preview_sample = [f"{r[1]} {r[2]} ({r[3]})" for r in matched[:20]]
                matched_list = [f"{r[0]}: {r[1]} {r[2]} ({r[3]})" for r in matched]

                action = request.form.get('action')
                if action == 'save' and preview_count > 0:
                    # create category code (include contest to scope it) — use short contest prefixes to fit DB column
                    contest = selected_contest
                    contest_map = {'runmagedon': 'RM', 'biegi': 'BG', 'plywanie': 'PL'}
                    contest_code = contest_map.get(contest, contest[:2].upper())
                    prefix = 'ALL' if gender == 'ALL' else ('M' if gender == 'M' else 'K')
                    category_code = f"{contest_code}_{prefix}_{start_year}-{end_year}"
                    # Ensure it fits into varchar(20); fall back to shorter form if needed
                    if len(category_code) > 20:
                        category_code = f"{contest_code}_{prefix}_{start_year}"
                        if len(category_code) > 20:
                            category_code = category_code[:20]

                    updated = 0
                    try:
                        for pid, im, naz, yr in matched:
                            if contest == 'runmagedon':
                                # update or insert runmagedon row
                                cur.execute("SELECT id FROM runmagedon WHERE id = ?", (pid,))
                                if cur.fetchone():
                                    cur.execute("UPDATE runmagedon SET kategoria = ? WHERE id = ?", (category_code, pid))
                                else:
                                    cur.execute("INSERT INTO runmagedon (id, kategoria) VALUES (?, ?)", (pid, category_code))
                                # link uczestnik.runmagedon
                                cur.execute("UPDATE uczestnik SET runmagedon = ? WHERE id = ?", (pid, pid))
                            else:
                                # store category in the chosen contest table (biegi or plywanie)
                                cur.execute(f"SELECT id FROM {contest} WHERE id = ?", (pid,))
                                if cur.fetchone():
                                    cur.execute(f"UPDATE {contest} SET kategoria = ? WHERE id = ?", (category_code, pid))
                                else:
                                    cur.execute(f"INSERT INTO {contest} (id, kategoria) VALUES (?, ?)", (pid, category_code))
                            updated += 1
                        conn.commit()
                        msg = f'Zapisano kategorię {category_code} do {contest} dla {updated} uczestników.'
                    except mariadb.Error as e:
                        conn.rollback()
                        if 'Data too long for column' in str(e):
                            msg = 'Błąd: nazwa kategorii jest zbyt długa dla kolumny. Zmień zakres lat lub wybierz inną opcję (użyj krótszego turnieju/zakresu).'
                        else:
                            msg = f'Błąd zapytania: {e}'
            except mariadb.Error as e:
                msg = f'Błąd zapytania: {e}'

    cur.close()
    conn.close()

    return render_template_string(KATEGORIE_TEMPLATE, top_link=top_link, msg=msg, preview_count=preview_count, preview_sample=preview_sample, matched_list=matched_list, min_year=min_year, max_year=max_year, selected_gender=selected_gender, selected_start_year=selected_start_year, selected_end_year=selected_end_year, selected_contest=selected_contest)


KATEGORIE_TEMPLATE = """
<html>
  <head>
    <meta charset="utf-8">
    <style>
      .form-row { margin-bottom: 8px }
      .btn { padding: 6px 10px; }
      .sample { font-size: 0.95em; color: #333 }
    </style>
  </head>
  <body>
    {{ top_link|safe }}
    <h1>Tworzenie kategorii</h1>
    {% if msg %}<p><strong>{{ msg }}</strong></p>{% endif %}

    <form method="post">
      <div class="form-row">
        <label>Płeć:
          <select name="gender">
            <option value="ALL" {% if selected_gender == 'ALL' %}selected{% endif %}>Obie</option>
            <option value="M" {% if selected_gender == 'M' %}selected{% endif %}>Mężczyzna</option>
            <option value="K" {% if selected_gender == 'K' %}selected{% endif %}>Kobieta</option>
          </select>
        </label>
      </div>

      <div class="form-row">
        <label>Turniej:
          <select name="contest">
            <option value="runmagedon" {% if selected_contest == 'runmagedon' %}selected{% endif %}>Runmagedon</option>
            <option value="biegi" {% if selected_contest == 'biegi' %}selected{% endif %}>Biegi</option>
            <option value="plywanie" {% if selected_contest == 'plywanie' %}selected{% endif %}>Pływanie</option>
          </select>
        </label>
      </div>

      <div class="form-row">
        <label>Rok początkowy: <input name="start_year" type="number" value="{{ selected_start_year }}" min="1900" max="2100"></label>
      </div>

      <div class="form-row">
        <label>Rok końcowy: <input name="end_year" type="number" value="{{ selected_end_year }}" min="1900" max="2100"></label>
      </div>

      <div class="form-row">
        <button class="btn" type="submit" name="action" value="preview">Podgląd (ile pasuje)</button>
        <button class="btn" type="submit" name="action" value="save">Zapisz kategorię (zapis do wybranego turnieju)</button>
      </div>
    </form>

    {% if preview_count is not none %}
      <h2>Wynik podglądu: {{ preview_count }} uczestników</h2>
      {% if preview_sample %}
        <div class="sample">Przykładowe osoby:<br>{{ preview_sample|join('<br>')|safe }}</div>
      {% endif %}

      {% if matched_list %}
        <details>
          <summary>Pokaż wszystkie osoby ({{ preview_count }})</summary>
          <div class="sample" style="margin-top:8px">{{ matched_list|join('<br>')|safe }}</div>
        </details>
      {% endif %}
    {% endif %}

  </body>
</html>
"""

@app.route("/zawody", methods=["GET", "POST"])
def zawody():
    """Manage competition results per category and discipline.

    - Choose discipline (biegi/plywanie/runmagedon)
    - Choose category (from runmagedon.kategoria)
    - Show participants in that category and allow entering results
    - Save writes to corresponding table (insert/update) and links runmagedon when needed
    """
    top_link = f'<a class="btn-link" href="{url_for("index")}">Powrót do strony głównej</a>'
    msg = None

    try:
        login = db_lib.get_db_data()
        conn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
        cur = conn.cursor()
    except mariadb.Error as e:
        return f"DB connection error: {e}", 500

    discipline = request.values.get('discipline', 'biegi')
    show_all = request.values.get('show_all') == '1'
    # Get available categories for the selected discipline
    try:
        if discipline in ('biegi', 'plywanie', 'runmagedon'):
            cur.execute(f"SELECT DISTINCT kategoria FROM {discipline} WHERE kategoria IS NOT NULL")
            categories = [r[0] for r in cur.fetchall()]
        else:
            categories = []
    except mariadb.Error:
        categories = []

    category = request.values.get('category', '')
    participants = []

    # Handle form save
    if request.method == 'POST' and request.form.get('action') == 'save':
        discipline = request.form.get('discipline', discipline)
        category = request.form.get('category', category)
        try:
            # iterate over posted results
            updated = 0
            for key, val in request.form.items():
                if key.startswith('res_') and discipline in ('biegi', 'plywanie'):
                    pid = int(key.split('_', 1)[1])
                    wynik = val.strip() or None
                    if wynik:
                        # upsert into chosen table
                        cur.execute(f"SELECT id FROM {discipline} WHERE id = ?", (pid,))
                        if cur.fetchone():
                            cur.execute(f"UPDATE {discipline} SET wynik = ?, kategoria = ? WHERE id = ?", (wynik, category, pid))
                        else:
                            cur.execute(f"INSERT INTO {discipline} (id, wynik, kategoria) VALUES (?, ?, ?)", (pid, wynik, category))
                        # ensure uczestnik.link if needed (for runmagedon we link later)
                        updated += 1
                elif discipline == 'runmagedon' and key.startswith('start_'):
                    pid = int(key.split('_', 1)[1])
                    start_val = request.form.get(f'start_{pid}', '').strip()
                    end_val = request.form.get(f'end_{pid}', '').strip()
                    if start_val and end_val:
                        try:
                            tstart = datetime.datetime.strptime(start_val, '%H:%M:%S').time()
                        except ValueError:
                            try:
                                tstart = datetime.datetime.strptime(start_val, '%H:%M').time()
                            except ValueError:
                                tstart = None
                        try:
                            tstop = datetime.datetime.strptime(end_val, '%H:%M:%S').time()
                        except ValueError:
                            try:
                                tstop = datetime.datetime.strptime(end_val, '%H:%M').time()
                            except ValueError:
                                tstop = None
                        wynik_str = None
                        if tstart and tstop:
                            # compute difference (using arbitrary same date)
                            dt1 = datetime.datetime.combine(datetime.date.today(), tstart)
                            dt2 = datetime.datetime.combine(datetime.date.today(), tstop)
                            if dt2 < dt1:
                                # assume finish next day
                                dt2 += datetime.timedelta(days=1)
                            wynik_td = dt2 - dt1
                            wynik_str = str(wynik_td).split('.')[0]
                        # upsert into runmagedon
                        cur.execute("SELECT id FROM runmagedon WHERE id = ?", (pid,))
                        if cur.fetchone():
                            cur.execute("UPDATE runmagedon SET czasStartu = ?, czasMety = ?, wynik = ?, kategoria = ? WHERE id = ?", (tstart, tstop, wynik_str, category, pid))
                        else:
                            cur.execute("INSERT INTO runmagedon (id, wynik, kategoria, czasStartu, czasMety) VALUES (?, ?, ?, ?, ?)", (pid, wynik_str, category, tstart, tstop))
                        # link uczestnik
                        cur.execute("UPDATE uczestnik SET runmagedon = ? WHERE id = ?", (pid, pid))
                        updated += 1
            conn.commit()
            msg = f'Zapisano wyniki: {updated} wpisów.'
        except mariadb.Error as e:
            conn.rollback()
            msg = f'Błąd zapisu: {e}'

    # If category chosen, show participants from that category (based on runmagedon.kategoria)
    if show_all or category:
        try:
            # Order by participant id so table follows `uczestnik` order
            if show_all:
                cur.execute("SELECT id, imie, nazwisko FROM uczestnik ORDER BY id")
            else:
                if discipline in ('biegi', 'plywanie'):
                    cur.execute(f"SELECT u.id, u.imie, u.nazwisko FROM uczestnik u JOIN {discipline} d ON d.id = u.id WHERE d.kategoria = ? ORDER BY u.id", (category,))
                else:
                    cur.execute("SELECT u.id, u.imie, u.nazwisko FROM uczestnik u JOIN runmagedon r ON r.id = u.id WHERE r.kategoria = ? ORDER BY u.id", (category,))
            participants = cur.fetchall()
        except mariadb.Error as e:
            cur.close(); conn.close()
            return f"DB query error: {e}", 500

    # For participants, fetch existing results for the selected discipline
    rows = []
    for p in participants:
        pid, im, naz = p
        if discipline in ('biegi', 'plywanie'):
            cur.execute(f"SELECT wynik FROM {discipline} WHERE id = ?", (pid,))
            r = cur.fetchone()
            val = r[0] if r and r[0] is not None else ''
            rows.append((pid, im, naz, val))
        else:  # runmagedon
            cur.execute("SELECT czasStartu, czasMety, wynik FROM runmagedon WHERE id = ?", (pid,))
            r = cur.fetchone()

            def _format_time_value(v):
                # Only None means missing value; zero timedelta/time should be shown as 00:00:00
                if v is None:
                    return ''
                # Time object
                if isinstance(v, datetime.time):
                    return v.strftime('%H:%M:%S')
                # Datetime object
                if isinstance(v, datetime.datetime):
                    return v.strftime('%H:%M:%S')
                # Timedelta -> format as HH:MM:SS (including zero timedelta)
                if isinstance(v, datetime.timedelta):
                    total = int(v.total_seconds())
                    h = total // 3600
                    m = (total % 3600) // 60
                    s = total % 60
                    return f"{h:02}:{m:02}:{s:02}"
                # Fallback to str
                return str(v)

            start = _format_time_value(r[0]) if r and len(r) > 0 else ''
            end = _format_time_value(r[1]) if r and len(r) > 1 else ''
            wynik = r[2] if r and r[2] else ''
            if isinstance(wynik, datetime.timedelta):
                wynik = _format_time_value(wynik)
            rows.append((pid, im, naz, start, end, wynik))

    cur.close()
    conn.close()

    template = """
    <!doctype html>
    <html lang="pl">
    <head>
      <meta charset="utf-8">
      <title>Zawody</title>
      <style>
        table { border-collapse: collapse; }
        th, td { border:1px solid #ccc; padding:6px 8px; }
        input.time { width: 90px }
        input.res { width: 120px }
      </style>
    </head>
    <body>
      {{ top_link|safe }}
      <h1>Zawody</h1>
      {% if msg %}<p><strong>{{ msg }}</strong></p>{% endif %}

      <form id="zawody_select_form" method="get">
        <div>
          <label>Dziedzina:
            <select name="discipline">
              <option value="biegi" {% if discipline == 'biegi' %}selected{% endif %}>Biegi</option>
              <option value="plywanie" {% if discipline == 'plywanie' %}selected{% endif %}>Pływanie</option>
              <option value="runmagedon" {% if discipline == 'runmagedon' %}selected{% endif %}>Runmagedon</option>
            </select>
          </label>

          <label style="margin-left:12px">Kategoria:
            <select name="category">
              <option value="">-- wybierz --</option>
              {% for c in categories %}
                <option value="{{ c }}" {% if c == category %}selected{% endif %}>{{ c }}</option>
              {% endfor %}
            </select>
          </label>

          <label style="margin-left:12px"><input type="checkbox" name="show_all" value="1" {% if show_all %}checked{% endif %}> Pokaż wszystkich (ignoruj kategorię)</label>

          <button type="submit" name="action" value="show">Pokaż</button>
        </div>
      </form>

      <script>
      document.addEventListener('DOMContentLoaded', function() {
        var form = document.getElementById('zawody_select_form');
        if (form) {
          var elements = form.querySelectorAll('select[name="discipline"], select[name="category"], input[name="show_all"]');
          elements.forEach(function(el){ el.addEventListener('change', function(){ form.submit(); }); });
        }
      });
      </script>

      {% if rows %}
        <form method="post">
          <input type="hidden" name="discipline" value="{{ discipline }}">
          <input type="hidden" name="category" value="{{ category }}">
          <input type="hidden" name="show_all" value="{% if show_all %}1{% else %}{% endif %}">
          <table>
            <thead>
              <tr>
                <th>Lp.</th>
                <th>Imię</th>
                <th>Nazwisko</th>
                {% if discipline == 'runmagedon' %}
                  <th>Start (HH:MM:SS)</th>
                  <th>Meta (HH:MM:SS)</th>
                  <th>Wynik</th>
                {% else %}
                  <th>Wynik</th>
                {% endif %}
              </tr>
            </thead>
            <tbody>
              {% for r in rows %}
                <tr>
                  <td>{{ loop.index }}</td>
                  <td>{{ r[1] }}</td>
                  <td>{{ r[2] }}</td>
                  {% if discipline == 'runmagedon' %}
                    <td><input class="time" name="start_{{ r[0] }}" value="{{ r[3] }}"></td>
                    <td><input class="time" name="end_{{ r[0] }}" value="{{ r[4] }}"></td>
                    <td>{{ r[5] }}</td>
                  {% else %}
                    <td><input class="res" name="res_{{ r[0] }}" value="{{ r[3] }}"></td>
                  {% endif %}
                </tr>
              {% endfor %}
            </tbody>
          </table>
          <p><button type="submit" name="action" value="save">Zapisz wyniki</button></p>
        </form>
      {% endif %}

    </body>
    </html>
    """

    return render_template_string(template, top_link=top_link, categories=categories, discipline=discipline, category=category, rows=rows, msg=msg, show_all=show_all)


LEGIT_TEMPLATE = """
<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <title>Generator Legitymacji</title>
  <style>
    .btn { padding: 6px 10px; margin-right: 8px }
    .btn-link { padding: 6px 8px; border: 1px solid gray; background:#f0f0f0; text-decoration:none; color:black }
    ul { margin-top:8px }
  </style>
</head>
<body>
  {{ top_link|safe }}
  <h1>Generator Legitymacji</h1>
  {% if msg %}<p><strong>{{ msg }}</strong></p>{% endif %}

  <form method="post">
    <button class="btn" name="action" value="generate" type="submit">Generuj legitymacje</button>
    {% if generated %}
      <a class="btn-link" href="{{ url_for('legitymacje_download') }}">Pobierz gotowy plik (legitymacje.pdf)</a>
    {% endif %}
    <button class="btn" name="action" value="check_missing" type="submit">Sprawdź brakujące imiona obozowe</button>
  </form>

  {% if missing_count is not none %}
    <h2>Brakujące imiona obozowe: {{ missing_count }}</h2>
    {% if missing_count > 0 %}
      <ul>
        {% for m in missing %}
          <li>{{ m }}</li>
        {% endfor %}
      </ul>
    {% else %}
      <p>Brak brakujących wpisów — wszystko wypełnione.</p>
    {% endif %}
  {% endif %}

</body>
</html>
"""


@app.route('/zajecia', methods=['GET', 'POST'])
def zajecia():
    """Manage wychowawca zajecia and view participants' assigned zajecia."""
    top_link = f'<a class="btn-link" href="{url_for("index")}">Powrót do strony głównej</a>'
    msg = None

    try:
        login = db_lib.get_db_data()
        conn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
        cur = conn.cursor()
    except mariadb.Error as e:
        return f"DB connection error: {e}", 500

    # Handle updates to wychowawca.zajecia
    if request.method == 'POST':
        updates = []
        for key, val in request.form.items():
            if not key.startswith('zaj_'):
                continue
            try:
                wid = int(key.split('_', 1)[1])
            except Exception:
                continue
            v = val.strip() or None
            updates.append((v, wid))
        if updates:
            try:
                for v, wid in updates:
                    cur.execute("UPDATE wychowawca SET zajecia = ? WHERE id = ?", (v, wid))
                conn.commit()
                msg = 'Zapisano zajęcia.'
            except mariadb.Error as e:
                conn.rollback()
                msg = f'Błąd zapisu: {e}'

    try:
        cur.execute("SELECT id, imie, nazwisko, zajecia FROM wychowawca ORDER BY id")
        wych = cur.fetchall()
    except mariadb.Error as e:
        cur.close(); conn.close()
        return f"DB query error: {e}", 500

    # We no longer render the full participants lists on this page (keeps UI compact)
    cur.close()
    conn.close()

    template = """
    <!doctype html>
    <html lang="pl">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Zajęcia</title>
      <style>
        :root{--pad:12px;}
        body { font-family: Arial, sans-serif; padding: 16px; color: #111; background: #fff; }
        h1 { font-size: 1.5rem; margin-bottom: 8px }
        h2 { font-size: 1.1rem; margin-top: 12px }
        .table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; margin-bottom: 12px }
        table { border-collapse: collapse; width: 100%; min-width: 420px }
        th, td { padding: 8px 10px; border:1px solid #ccc; text-align: left }
        input.text { width: 100%; box-sizing: border-box; padding: 6px }
        .btn { display:inline-block; padding: 8px 12px; background:#f0f0f0; border:1px solid #ccc; cursor:pointer }
        @media (max-width: 600px) {
          body { padding: 10px; font-size: 15px }
          table { min-width: 360px }
          th, td { padding: 10px 8px }
          h1 { font-size: 1.25rem }
        }
      </style>
    </head>
    <body>
      {{ top_link|safe }}
      <h1>Zajęcia</h1>
      {% if msg %}<p><strong>{{ msg }}</strong></p>{% endif %}

      <h2>Edytuj zajęcia wychowawców</h2>
      <form method="post">
      <div class="table-wrap">
      <table>
        <thead><tr><th>Lp.</th><th>Wychowawca</th><th>Zajęcia</th></tr></thead>
        <tbody>
        {% for w in wych %}
          <tr>
            <td>{{ loop.index }}</td>
            <td>{{ w[1] }} {{ w[2] }}</td>
            <td><input class="text" name="zaj_{{ w[0] }}" value="{{ w[3] or '' }}"></td>
          </tr>
        {% endfor %}
        </tbody>
      </table>
      </div>
      <p><button class="btn" type="submit">Zapisz zmiany</button></p>
      </form>

    <!-- Participant lists hidden on this page (kept minimal). If you need them, use the 'Grupy innych' or specific group pages. -->

    </body>
    </html>
    """

    return render_template_string(template, top_link=top_link, wych=wych, msg=msg)


@app.route("/legitymacje", methods=["GET", "POST"])
def legitymacje():
    """Display a page to generate and download Legitymacje and to check missing camp names.

    - GET: show buttons and status
    - POST action=generate: run generator and show download link when ready
    - POST action=check_missing: show count and list of participants with pierwszyRaz='tak' and no imieObozowe
    """
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'legitymacja', 'legitymacja.py'))
    output_path = os.path.abspath(os.path.join(os.path.dirname(script_path), 'output', 'to_print.pdf'))

    msg = None
    generated = os.path.exists(output_path)
    missing = []
    missing_count = None

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'generate':
            # Check for first-time participants missing camp names and count how many will be generated
            try:
                login = db_lib.get_db_data()
                cconn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
                ccur = cconn.cursor()
                ccur.execute("SELECT COUNT(*) FROM uczestnik WHERE pierwszyRaz = 'tak'")
                total_first = ccur.fetchone()[0] or 0
                ccur.execute("SELECT id, imie, nazwisko FROM uczestnik WHERE pierwszyRaz = 'tak' AND (imieObozowe IS NULL OR imieObozowe = '') ORDER BY id")
                missing_rows = ccur.fetchall()
                missing = [f"{r[0]}: {r[1]} {r[2]}" for r in missing_rows]
                missing_count = len(missing)
                ccur.execute("SELECT COUNT(*) FROM uczestnik WHERE pierwszyRaz = 'tak' AND imieObozowe IS NOT NULL AND imieObozowe <> ''")
                with_name = ccur.fetchone()[0] or 0
                ccur.close()
                cconn.close()
            except mariadb.Error as e:
                # If DB check fails, leave previous missing info as-is and continue
                missing = missing or []
                missing_count = missing_count if missing_count is not None else None
                total_first = None
                with_name = None

            # Remove previous output if present
            try:
                if os.path.exists(output_path):
                    os.remove(output_path)
            except Exception:
                pass

            try:
                res = subprocess.run([sys.executable, script_path, '-d'], check=True, cwd=os.path.dirname(script_path), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=60)
                generated = os.path.exists(output_path)
                if generated:
                    if missing_count and missing_count > 0:
                        # Inform user how many were generated and how many skipped
                        msg = f'Generacja zakończona. Wygenerowano {with_name} kart, pominięto {missing_count} uczestników bez imion obozowych.'
                    else:
                        msg = 'Generacja zakończona pomyślnie. Plik gotowy do pobrania.'
                else:
                    msg = 'Generacja zakończona, ale plik nie został znaleziony.'
            except subprocess.CalledProcessError as e:
                err = e.stderr or e.stdout or str(e)
                msg = f'Błąd generowania: {err}'
            except Exception as e:
                msg = f'Błąd uruchomienia generatora: {e}'

        elif action == 'check_missing':
            try:
                login = db_lib.get_db_data()
                conn = mariadb.connect(user=login['user'], password=login['password'], host=login['host'], database=login['database'])
                cur = conn.cursor()
                cur.execute("SELECT id, imie, nazwisko FROM uczestnik WHERE pierwszyRaz = 'tak' AND (imieObozowe IS NULL OR imieObozowe = '') ORDER BY id")
                rows = cur.fetchall()
                cur.close()
                conn.close()
                missing = [f"{r[0]}: {r[1]} {r[2]}" for r in rows]
                missing_count = len(missing)
                msg = f'Znaleziono {missing_count} uczestników bez imion obozowych.'
            except mariadb.Error as e:
                msg = f'Błąd przy sprawdzaniu braków: {e}'

    top_link = f'<a class="btn-link" href="{url_for("index")}">Powrót do strony głównej</a>'
    return render_template_string(LEGIT_TEMPLATE, top_link=top_link, msg=msg, generated=generated, missing=missing, missing_count=missing_count)


@app.route('/legitymacje/download')
def legitymacje_download():
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'legitymacja', 'legitymacja.py'))
    output_path = os.path.abspath(os.path.join(os.path.dirname(script_path), 'output', 'to_print.pdf'))
    if not os.path.exists(output_path):
        return redirect(url_for('legitymacje'))
    return send_file(output_path, as_attachment=True, download_name='legitymacje.pdf')

if __name__ == "__main__":
    app.run(debug=True)
