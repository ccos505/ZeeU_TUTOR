import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_questions(filename):
    file_path = os.path.join(BASE_DIR, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)