#!/usr/bin/env -S python3 -u

from PIL import Image, ImageDraw, ImageFont
import datetime
import random
import mariadb

import os
import sys

import db_lib

card_width = 1096
card_hight = 620
tiles_x = 2
tiles_y = 5
tile_start_x=148 
tile_start_y=261

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


template_path = os.path.join(os.path.dirname(__file__), "legitymacje/template.png")

georgia_font = os.path.join(os.path.dirname(__file__), "legitymacje/fonts/georgia.ttf")
linlibretine_font = os.path.join(os.path.dirname(__file__), "legitymacje/fonts/LinLibertine_DR.otf")
linlibretine_BI_font = os.path.join(os.path.dirname(__file__), "legitymacje/fonts/LinLibertine_RBI.otf")
linlibretine_B_font = os.path.join(os.path.dirname(__file__), "legitymacje/fonts/LinLibertine_RB.otf")
gabriola_font = os.path.join(os.path.dirname(__file__), "legitymacje/fonts/gabriola.ttf")

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
    
def get_names_from_db():
    conn, cursor = connect_to_db()
    
    if conn == None or cursor == None:
        sys.exit(1)
    
    people_list = []
    
    try:
        # Only select first-timers who already have an imieObozowe filled
        cursor.execute("SELECT imie, nazwisko, imieObozowe FROM uczestnik WHERE pierwszyRaz = 'tak' AND imieObozowe IS NOT NULL AND imieObozowe <> '' ORDER BY id")
        for row in cursor:
            # row[2] (imieObozowe) is guaranteed to be non-empty here
            people_list.append([row[0] + " " + row[1], row[2]])
    except mariadb.Error as e:
        print(f"Error: {e}")
        people_list = []
        
    conn.commit()
    cursor.close()        
    conn.close()
    return people_list
    

def generate_card(name, new_name, template = True):
    
    font_title = ImageFont.truetype(linlibretine_B_font, 60)
    font_name = ImageFont.truetype(gabriola_font, 70)
    font_new_name = ImageFont.truetype(linlibretine_BI_font, 60)  
    font_description = ImageFont.truetype(linlibretine_font, 50)
    font_footer = ImageFont.truetype(linlibretine_font, 40)

    if template:
        card = Image.open(template_path)
    
        draw = ImageDraw.Draw(card)

        draw.text((30, 180), name, fill="black", font=font_name)
        draw.text((30, 430), new_name, fill="black", font=font_new_name)
    else:
        card = Image.new("RGBA", (1096, 620), "white")
        logo = Image.open(os.path.join(os.path.dirname(__file__),"logo.png")).convert("RGBA")

        draw = ImageDraw.Draw(card)

        card.paste(logo, (620, 40), logo)
        draw.rectangle([0, 0, 1095, 619], outline="black", width=2)

        draw.text((30, 50), "Legitymacja Chrztu", fill="black", font=font_title)
        draw.text((30, 180), name, fill="black", font=font_name)
        draw.text((30, 300), "KADRA \"RUSZ TYŁEK!\"\nNADAJE CI IMIĘ OBOZOWE:\n", fill="black", font=font_description)
        draw.text((30, 430), new_name, fill="black", font=font_new_name)
        draw.text((30, 550), f"Okoniny Nadjeziorne {datetime.datetime.now().year}", fill="black", font=font_footer)

    return card

def generate_random_card():

    return generate_card(names[random.randrange(0, 19)] + " " + surnames[random.randrange(0, 19)], nicknames_first[random.randrange(0, 19)] + " " + nicknames_second[random.randrange(0, 19)])

def tile_cards(cards_list):
    tile_pages = []
    
    done_cards_counter = 0
    current_page = -1
    x = tile_start_x
    y = tile_start_y
    while len(cards_list) > 0:
        if (done_cards_counter % (tiles_x * tiles_y)) == 0:
            tile_pages.append(Image.new("RGBA", (2480, 3508), "white"))
            x = tile_start_x
            y = tile_start_y
            current_page = current_page + 1
        
        tile_pages[current_page].paste(cards_list.pop(0), (x, y))
        x = x + card_width
        if (done_cards_counter % tiles_x) == (tiles_x - 1):
            x = tile_start_x
            y = y + card_hight
        
        done_cards_counter = done_cards_counter + 1

    return tile_pages

def tile_random_cards(cards_number):
    cards = []
    for _ in range(cards_number):
        cards.append(generate_random_card())
    
    return tile_cards(cards)

def generate_template():
    generate_card("", "", False).save(template_path)

def output_random(cards_number):
    output_from_list(generate_random_list(cards_number))
        
def generate_random_list(length):
    random_list = []
    for n in range(length):
        random_list.append([names[random.randrange(0, 19)] + " " + surnames[random.randrange(0, 19)], nicknames_first[random.randrange(0, 19)] + " " + nicknames_second[random.randrange(0, 19)]])
    return random_list
       
def output_from_list(name_list):
    if not name_list:
        print("No names provided — nothing to generate.")
        return

    list_of_cards = []
    skipped = 0
    for person in name_list:
        name = person[0] if len(person) > 0 else None
        new_name = person[1] if len(person) > 1 else None
        if not name or not new_name:
            print(f"Skipping entry (missing name or camp name): {name!r}, {new_name!r}")
            skipped += 1
            continue
        list_of_cards.append(generate_card(name, new_name))

    if not list_of_cards:
        print("No valid cards to generate after filtering missing names.")
        return

    if skipped:
        print(f"Skipped {skipped} entries due to missing data.")

    sheets = tile_cards(list_of_cards)
    rgb_sheets = [sheet.convert("RGB") for sheet in sheets]
    output_path = os.path.join(os.path.dirname(__file__), "legitymacje/output/to_print.pdf")
    if rgb_sheets:
        rgb_sheets[0].save(
            output_path,
            "PDF",
            save_all=True,
            append_images=rgb_sheets[1:]
        )

if __name__ == "__main__":
    
    arguments = sys.argv
    
    if len(arguments) > 1:
        match arguments[1]:
            case '-h' | '--help':
                print("Rusztyłkowa Legitymacja generator:\n -h or --help - see avaliable options\n -t - generate template\n -d - generate cards using db as source\n -r - generate cards with random names - followed by number of cards\n -m - generate cards manually - followed by names and nickname\n -a - add manually generated cards to others - followed by names and nickname, use with only with -d\nArguments formating for -m -a options: 'name1' 'nickname1' 'name2' 'nickname2' ...")
            case '-t':
                generate_template()
                print("Template done")
            case'-m':
                name_args = arguments[2:]
                if len(name_args) % 2 == 0 and len(name_args) != 0:
                    name_list = [[name_args[i], name_args[i + 1]] for i in range(0, len(name_args), 2)]
                    output_from_list(name_list)
                    print("Cards generated")
                else:
                    print("Names or nickname missing")                
            case '-d':
                output_from_list(get_names_from_db())
            case '-ad' | '-da':
                name_args = arguments[2:]
                if len(name_args) % 2 == 0 and len(name_args) != 0:
                    additional_name_list = [[name_args[i], name_args[i + 1]] for i in range(0, len(name_args), 2)]
                    output_from_list(get_names_from_db() + additional_name_list)
                    print("Cards generated")
                else:
                    print("Names or nickname missing")
            case '-r':
                if len(arguments) == 3:
                    try:
                        card_number = int(arguments[2])
                    except:
                        print("Second argument must be an integer")
                    print(f"Generating {card_number} cards")
                    output_from_list(generate_random_list(card_number))
                    print("Cards generated")
                else:
                    if len(arguments) < 3:
                        print("Too few arguments")
                    else:
                        print("Too many arguments")
            case _: 
                print("Rusztyłkowa Legitymacja generator:\nUse -h or --help")
                
    else:
        print("Rusztyłkowa Legitymacja generator:\nUse -h or --help")