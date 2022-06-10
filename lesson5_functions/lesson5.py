LOGGING = True
SORT_BY_NUMBER = True
key = "name"


team: list[dict] = [
    {"name": "John", "age": 20, "number": 8},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Amber", "age": 17, "number": 12},
]


def repr_players(players: list[dict], sorted: bool, key: str) -> None:
    print("TEAM:")
    if sorted and not key != None:
        team.sort(key=lambda x: x["number"])
        log(message="Sort by number")
        display_team(team)

    elif sorted and not key == None:
        team.sort(key=lambda x: x[key])
        log(message=f"Sort by {key}")
        display_team(team)

    else:
        display_team(team)
        print("\n")


def display_team(players: dict):
    for player in players:
        print(f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}")


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <-")


def add_player(num: int, name: str, age: int) -> None:
    player = {"name": name, "number": num, "age": age}
    checking_result = check_existing_by_number(team, num)
    if checking_result == True:
        team.append(player)
        log(message=f"Adding {player['name']}")
        display_team(team)
    else:
        print("Cant add player. Player with this number already exist!")


def check_existing_by_number(players: list, new_number: int) -> bool:
    for index, player in enumerate(players):
        if player["number"] != new_number:
            return True
        else:
            return False


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def main():
    add_player(num=13, name="Cris", age=31)
    repr_players(team, SORT_BY_NUMBER, key=None)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")


def sort_by_age(players: list) -> list:
    team.sort(key=lambda x: x["age"])
    return list
