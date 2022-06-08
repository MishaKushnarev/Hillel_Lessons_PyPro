from typing import Generator


FILENAME = "./lesson4_iter_gener_functions/rockyou.txt"
SEARCH_KEYWORD = "user"
result = []
count_items = int()


def read_lines_find_user_generator() -> Generator:
    
    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()            
            if not line:
                print("Scanning done! Added", count_items, "items.")
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")                               
                continue


for line in read_lines_find_user_generator():
    print("Now password is: ", line)
    choice = str(input("Keep? (y/n): "))
    if choice == "y":
        result.append(line)
        count_items += 1