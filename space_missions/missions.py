
missions_data = [
    {
        "name": "Mars 2020",
        "year": 2020,
        "direction": "Марс"
    },
    {
        "name": "Artemis I",
        "year": 2022,
        "direction": "Луна"
    },
    {
        "name": "Voyager 1",
        "year": 1977,
        "direction": "Дальний космос"
    },
    {
        "name": "Chandrayaan-3",
        "year": 2023,
        "direction": "Луна"
    }
]

def get_all_missions():
    return missions_data

def search_missions_by_direction(direction):
    # Ищем миссии, где направление совпадает (без учета регистра)
    results = [m for m in missions_data if m["direction"].lower() == direction.lower()]
    return results
