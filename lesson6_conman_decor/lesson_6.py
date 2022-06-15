import functools
import os


# MODIFY THIS DECORATOR
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data = func()
        if type(data) == str:
            result_string = data[::-1]
        else:
            pass

    return wrapper


# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


# TEST OUPUT
os.system("cls||clear")
print(get_university_name(), get_university_founding_year(), sep="\n")


# MODIFY THIS DECORATOR
def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tmp_list = []
            data = func(*args, **kwargs)

            for name in data["name"]:
                tmp_list.append(name)

                for i in range(len(tmp_list)):
                    tmp_list[i] = "*"
                    result_list = "".join(tmp_list)
                    data["name"] = result_list

            return data

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUTPUT
os.system("cls||clear")
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
