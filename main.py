# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True


    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (first_name, nick_name) VALUES
    #         ('Den', 'barracuda' );"""
    #
    #     )
    #     print("[INFO] data was successfully inserted")

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT  nick_name FROM users WHERE first_name = 'Den';"""

        )
        print(cursor.fetchone())

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if connection:
       # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")