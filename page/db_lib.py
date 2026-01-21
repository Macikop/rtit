import json
import os

cridentials_path = os.path.join(os.path.dirname(__file__), "../../db_info.json")

def get_db_data(path=cridentials_path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)    
    return data
