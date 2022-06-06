# TEST
**TEST**

```Python
def write_to_temp(file_name, some_dict) -> None:

    with open(file_name, "w") as temp_file:
        json.dump(some_dict, temp_file, indent=4)
```