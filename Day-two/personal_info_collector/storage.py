import json

FILE_NAME = "persons.json"

def save_to_file(persons):
    """Save list of persons to JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump([p.__dict__ for p in persons], f, indent=4)

def load_from_file():
    """Load persons from JSON file."""
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            from models import Person
            return [Person(**p) for p in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
