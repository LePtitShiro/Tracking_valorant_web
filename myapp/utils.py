import json
from random import randint, shuffle

from werkzeug.datastructures.structures import ImmutableDict

path : str = "./data/player_data.json"
users_data_path : str = "./data/users_data.json"

def get_data() -> dict:
    with open(path, "r") as f:
        data = json.load(f)
    return data

def get_player(player_id) -> dict:
    data = get_data()
    return data["players"][player_id]

def add_new_key(player: str, key: str, value: str) -> None:
    data = get_data()
    data['players'][player][key] = value

    with open(path, "w") as f:
        json.dump(data, f)

# def sup(key:str):
#     value = ""
#     for k in key:
#         if k != "#":
#             value += k
#         else:
#             return value

# agents = [
#     "Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Fade", "Harbor",
#     "Jett", "KAY/O", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna",
#     "Sage", "Skye", "Sova","Vyse", "Viper", "Yoru"]
#
# for player in get_data()['players']:
#     add_new_key(player, "username", sup(get_player(player)['riot_id']))
#     a = randint(0, 100)
#     b = randint(0, 100)
#     c = randint(0, 100)
#     add_new_key(player, "total_wins", str(a))
#     add_new_key(player, "total_loses", str(b))
#     add_new_key(player, "total_draws", str(c))
#     add_new_key(player, "total_games", str(a + b + c))
#     add_new_key(player, "agent", agents[randint(0, len(agents) - 1)])
#     add_new_key(player, "times_played", str((a + b + c) * 2))
#     add_new_key(player, "hs", str(randint(15, 100)))


def get_users_data() -> dict:
    with open(users_data_path, "r") as f:
        data = json.load(f)
    return data


def add_user(form: ImmutableDict[str,str]) -> None:
    data = get_users_data()
    new_id = create_id()
    data['users'][new_id] = transform_data(form)
    with open(users_data_path, "w") as f:
        json.dump(data, f)

def create_id() -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        id = ''.join(alphabet[randint(0, 25)] + str(randint(0, 9)) for _ in range(5))
        if id not in get_users_data()['users']:
            return id

def transform_data(data: ImmutableDict[str,str]) -> dict:
    return {
        "username": data['username'],
        "password": data['password'],
        "email": data['email'],
        "riot_id": data['riot_id'],}


def check_user(form: ImmutableDict[str,str]) -> bool:
    data = get_users_data()
    for user in data['users']:
        if data['users'][user]['username'].equals(form['username']) and data['users'][user]['password'].equals(form['password']):
            return True
    return False