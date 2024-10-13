import json
from random import randint

path : str = "./data/player_data.json"

def get_data() -> dict:
    with open(path, "r") as f:
        data = json.load(f)
    return data

def get_player(player_id) -> dict:
    data = get_data()
    return data['players'][player_id]

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

