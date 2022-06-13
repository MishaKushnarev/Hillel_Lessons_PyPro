import os
import copy


LOGGING = True
SORT_BY_NUMBER = True
key = "name"


team: list[dict] = [
    {"name": "John", "age": 20, "number": 8},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Amber", "age": 17, "number": 12},
]


def repr_players(players: list[dict], sorted: bool, key: str) -> None:

    if sorted and not key != None:
        team.sort(key=lambda x: x['number'])
        log(message=f"TEAM (sort by number):")
        display_team(team)

    elif sorted and not key == None:
        team.sort(key=lambda x: x[key])
        log(message=f"TEAM sort by {key}:")
        display_team(team)

    else:
        display_team(team)
        print("\n")


def display_team(players: dict):
    for player in players:
        print(f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}")


def log(message: str) -> None:
    print(f"{message}")


def add_player(num: int, name: str, age: int) -> None:
    player = {"name": name, "number": num, "age": age}
    checking_result = check_existing_by_number(team, num)
    if checking_result == False:
        log(message=f"Player {player['name']} added")
        team.append(player)
        repr_players(team, SORT_BY_NUMBER, key=None)
    else:
        print("Err")    


def check_existing_by_number(players: list, new_number: int) -> bool:
    for index, player in enumerate(players):
        if player['number'] == new_number:            
            log(message="Cant add player. Player with this number already exist!")
        else:
            return False    


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player['number'] == num:
            player_name = player['name']
            del players[index]
            log(message=f"Deleting {player_name}")


def player_update(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            log(message=f"Selected player: {player['number']} " f"{player['name']}, {player['age']}")
            temp_player = player
    user_choice = int(input('''What do you want to change? \n
        1 - Number
        2 - Name
        3 - Age
        Enter: ''' ))

    if user_choice == 1:
        new_number = int(input("Enter new number: "))
        # check_existing_by_number(players, new_number)
        temp_player['number'] = new_number
        os.system('cls||clear')
        log(message="Number updated!")
        repr_players(team, SORT_BY_NUMBER, key=None)

    elif  user_choice == 2:
        new_name = input("Enter new name: ")
        temp_player['name'] = new_name
        os.system('cls||clear')
        log(message="Name updated!")
        repr_players(team, SORT_BY_NUMBER, key=None)
        
    elif  user_choice == 3:
        new_age = input("Enter new age: ")
        temp_player["age"] = new_age
        os.system('cls||clear')
        log(message="Age updated!")
        repr_players(team, SORT_BY_NUMBER, key=None)
    else:
        pass


def main():
    os.system('cls||clear')
    add_player(num=12, name="Cris", age=31)   
    # repr_players(team, SORT_BY_NUMBER, key=None)
    # player_update(team, 8)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")


def sort_by_age(players: list) -> list:
    team.sort(key=lambda x: x["age"])
    return list
