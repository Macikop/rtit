# To generate 1000 records, you can use Python to append random rows based on the structure above.
import csv
import random
import os
from datetime import datetime, timedelta

header = [
    "id","Imię","Nazwisko","Turnus","Data urodzenia",
    "Czy pierwszy raz","Płeć dziecka","Czy dziecko zażywa leki?","Uwagi","rodo"
]

imiona = [
    "Adam", "Adrian", "Agnieszka", "Aleksander", "Aleksandra",
    "Alicja", "Andrzej", "Anna", "Barbara", "Bartosz",
    "Beata", "Bogdan", "Bogusław", "Bolesław", "Cezary",
    "Celina", "Dariusz", "Daniel", "Dawid", "Dominik",
    "Dorota", "Ewa", "Elżbieta", "Emil", "Emilia",
    "Eryk", "Filip", "Franciszek", "Gabriela", "Grzegorz",
    "Gustaw", "Halina", "Henryk", "Hubert", "Irena",
    "Iwona", "Igor", "Ignacy", "Ireneusz", "Jakub",
    "Jan", "Janina", "Jarosław", "Joanna", "Jerzy",
    "Józef", "Julia", "Julian", "Kacper", "Karol",
    "Karolina", "Kaja", "Katarzyna", "Kazimierz", "Kinga",
    "Krzysztof", "Łukasz", "Lech", "Lena", "Leonard",
    "Leszek", "Lucyna", "Łucja", "Lucjan", "Lidia",
    "Maciej", "Magdalena", "Marek", "Maria", "Marcin",
    "Marlena", "Marta", "Mateusz", "Mieczysław", "Mirosław",
    "Mikołaj", "Monika", "Natalia", "Natan", "Norbert",
    "Oliwia", "Olga", "Oskar", "Paweł", "Patryk",
    "Piotr", "Przemysław", "Radosław", "Renata", "Robert",
    "Roman", "Róża", "Sabina", "Sławomir", "Stanisław",
    "Stefan", "Szymon", "Tomasz", "Teresa", "Wiktoria"
]
# split names heuristically: names ending with 'a' treated as female
imiona_m = [n for n in imiona if not n.endswith('a')]
imiona_f = [n for n in imiona if n.endswith('a')]

nazwiska = [
    "Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk",
    "Kamiński", "Lewandowski", "Zieliński", "Szymański", "Woźniak",
    "Dąbrowski", "Kozłowski", "Jankowski", "Mazur", "Wojciechowski",
    "Kwiatkowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski",
    "Zawadzki", "Pawłowski", "Michalak", "Nowicki", "Wieczorek",
    "Jabłoński", "Malinowski", "Walczak", "Nowacki", "Rutkowski",
    "Olszewski", "Pawlak", "Sikora", "Czerwiński", "Kubiak",
    "Kozak", "Szulc", "Baran", "Góra", "Lipiński",
    "Chmielewski", "Mazurek", "Stępień", "Michałowski", "Bąk",
    "Andrzejewski", "Sikorski", "Czajkowski", "Zielińska", "Sosnowski",
    "Marciniak", "Borkowski", "Kalinowski", "Kaczmarczyk", "Brzeziński",
    "Wróbel", "Jakubowski", "Szczepański", "Konieczny", "Głowacki",
    "Sawicki", "Kruk", "Sobczak", "Sokołowski", "Dudek",
    "Kozieł", "Ostrowski", "Rybicki", "Wawrzyniak", "Wilk",
    "Urban", "Kurek", "Gajewski", "Bielawski", "Górski",
    "Szymczak", "Kot", "Przybylski", "Ziółkowski", "Turczyk",
    "Stankiewicz", "Walczak", "Kaczor", "Marcinek", "Rogowski",
    "Ciesielski", "Sroka", "Woliński", "Kacprzak", "Kostrzewa",
    "Mikołajczyk", "Błaszczyk", "Piątek", "Kubiak", "Walentynowicz",
    "Żuk", "Strzelecki", "Kurek", "Wesołowski", "Szczepaniak"
]
turnusy = ["1", "2", "3", "4"]
plec = ["Mężczyzna", "Kobieta"]
leki = ["Tak", "Nie"]
pierwszy_raz = ["tak", "nie"]
uwagi = [
    "jest pomocny.",
    "lubi śpiewać.",
    "uwielbia przygody.",
    "kocha zwierzęta.",
    "jest ambitny.",
    "lubi tańczyć.",
    "ceni porządek.",
    "jest wrażliwa.",
    "lubi wygrywać.",
    "jest towarzyska.", "", "","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",
]
rodo = ["Akceptuje"]

def random_date(start, end):
    delta = end - start
    int_delta = delta.days * 24 * 60 * 60 + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

def random_birthdate():
    start = datetime.strptime('2006-01-01', '%Y-%m-%d')
    end = datetime.strptime('2019-12-31', '%Y-%m-%d')
    return random_date(start, end).strftime('%Y-%m-%d')

def random_timestamp():
    start = datetime.strptime('2025-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime('2025-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')
    dt = random_date(start, end)
    return dt.strftime('%Y/%m/%d %I:%M:%S %p EEST')

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'uczestnicy.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        rows = 1000
        writer.writerow(["id","Imię","Nazwisko","Turnus","Data urodzenia","Czy pierwszy raz","Płeć dziecka","Czy dziecko zażywa leki?","Uwagi","rodo"])
        for _ in range(rows):
            gender = random.choice(plec)
            if gender == "Mężczyzna":
                imie_w = random.choice(imiona_m) if imiona_m else random.choice(imiona)
            else:
                imie_w = random.choice(imiona_f) if imiona_f else random.choice(imiona)

            row = [
                random_timestamp(),
                imie_w,
                random.choice(nazwiska),
                random.choice(turnusy),
                random_birthdate(),
                random.choice(pierwszy_raz),
                gender,
                random.choice(leki),
                random.choice(uwagi),
                "Akceptuje"
            ]
            writer.writerow(row)