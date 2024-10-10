import json

path : str = "./data/player_data.json"

def get_data() -> dict:
    with open(path, "r") as f:
        data = json.load(f)
    return data["players"]

def get_player(player_id) -> dict:
    data = get_data()
    return data[player_id]