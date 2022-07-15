# import asyncio
# import random
# from threading import Thread
# from typing import List

# # RND_MIN_VALUE = 1
# # COUNT_ELEMENTS = 1000000

# # def random_element(min_value1: int, max_value2: int) -> int:
# #     return random.randint(min_value1, max_value2)


# # def T1(count: int) -> List:
# #     result_list = []

# #     for _ in range(0, count):
# #         result_list.append(random_element(RND_MIN_VALUE, COUNT_ELEMENTS))

# #     return result_list


# # def T2(data: list) -> int:
# #     summ = 0

# #     for element in data:
# #         summ = summ + element
# #     print(f"Summ is : {summ}")
# #     return summ


# # def T3(count: int, summ: int) -> int:
# #     result = round(count / summ)

# #     return print("Average is: ", result)


# # def main():
# #     data = Thread(target=T1, args=(COUNT_ELEMENTS, ))
# #     summ = Thread(target=T2, args=(T1(COUNT_ELEMENTS), ))
# #     average = Thread(target=T3, args=(T2(T1(COUNT_ELEMENTS)), COUNT_ELEMENTS))

# #     data.start()
# #     data.join()
# #     summ.start()
# #     average.start()

# # if __name__ == '__main__':
# #     main()


# def get_primes_amount(num: int) -> int:
#     Results = 0

#     for i in num:
#         counter = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 counter += 1
#             if counter > 2:
#                 break
#         results += 1

#     return results


# numbers = [40000, 400, 1000000, 700]


# def main():
#     for i in numbers:
#         get_primes_amount(i)


# if __name__ == "__main__":
#     main()
