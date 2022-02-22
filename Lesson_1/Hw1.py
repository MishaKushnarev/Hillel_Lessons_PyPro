import os
import sqlite3

from typing import List


def execute_query(query_sql: str) -> List:
    '''
    Func for execute query
    :param query_sql: query
    :return: result
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def unwrapper(records: List) -> None:
    '''
    Func for print result
    :param records: response DB list
    :return:
    '''
    for record in records:
        print(*record)


def get_invoice_items() -> List:
    query_sql = f'SELECT UnitPrice, Quantity FROM invoice_items'

    return execute_query(query_sql)

unwrapper(get_invoice_items())
# def get_customers(state_name=None, city_name=None) -> None:
#     query_sql = ''' SELECT FirstName, City, State FROM customers'''
#     filter_query = 'WHERE'
#     if city_name and state_name:
#         filter_query += f"City = '{city_name}' and State = '{state_name}"
#         query_sql += filter_query
#     if city_name and not state_name:
#         filter_query += f"City = '{city_name}'"
#         query_sql += filter_query
#     if state_name and not city_name:
#         filter_query += f"State = '{state_name}'"
#         query_sql += filter_query
#     return unwrapper(execute_query(query_sql))


#get_customers(city_name='Budapest')

# def get_uniq_customers() -> None:
#     query_sql = 'SELECT FirstName FROM customers'
#     records = execute_query(query_sql)
#     result = set()
#     for record in records:
#         result.add(record[0])

#
# print(len(get_uniq_customers()))

# def get_uniq_customers() -> List:
#     query_sql = 'SELECT distinct FirstName FROM customers'
#     records = execute_query(query_sql)
#     result = []
#     for record in records:
#         result.append(record[0])
#     return result
# print(len(get_uniq_customers()))