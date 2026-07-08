import json
import os

DATABASE_FILE = "database/hashes.json"


def load_hashes():
    if not os.path.exists(DATABASE_FILE):
        return {}

    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    except:
        return {}


def save_hashes(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)