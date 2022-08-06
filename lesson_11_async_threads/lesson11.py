import asyncio
import random
from threading import Thread
from typing import List

RND_MIN_VALUE = 1
COUNT_ELEMENTS = 1000000
data = []


def random_element(min_value1: int, max_value2: int) -> int:
    return random.randint(min_value1, max_value2)


def T1(data: list, count: int) -> List:

    for _ in range(0, count):
        data.append(random_element(RND_MIN_VALUE, COUNT_ELEMENTS))

    return data


def T2(data: list) -> int:
    summ = 0

    for element in data:
        summ = summ + element
    print(f"Summ is : {summ}")
    return summ


def T3(data: list) -> int:
    result = round(sum(data) / len(data))

    return print("Average is: ", result)


def main():
    gen_data = Thread(target=T1, args=(data, COUNT_ELEMENTS))
    summ = Thread(target=T2, args=(data,))
    average = Thread(target=T3, args=(data,))

    gen_data.start()
    gen_data.join()
    summ.start()
    average.start()


if __name__ == "__main__":
    main()


async def get_primes_amount(number: int):
    sum = 0
    counter = 0
    for number in number:
        for num in range(1, number):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                sum += 1
                counter += 1
        print(counter)
        await asyncio.sleep(0)
    print(f"Summ is: {sum}")


def main(data: list) -> None:

    task = [get_primes_amount(data)]
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*task))
    event_loop.close()


if __name__ == "__main__":
    numbers = [500, 400, 1000, 700]
    main(numbers)
