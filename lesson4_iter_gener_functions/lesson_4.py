from typing import Generator

FILENAME = "./lesson4_iter_gener_functions/rockyou.txt"
SEARCH_KEYWORD = "user"
result = []
count_items = int()


def read_lines_find_user_generator() -> Generator:
    with open(FILENAME) as file:
        while True:
            line = file.readline()
            if not line:
                break
            elif SEARCH_KEYWORD in line:
                yield line.replace("\n", "")
    print("Scanning done! Added", count_items, "items.\n", result)


for line in read_lines_find_user_generator():
    print("Now password is: ", line)
    choice = str(input("Keep? (y/n): "))
    if choice == "y":
        result.append(line)
        count_items += 1
    else:
        pass
