import psycopg2
from datetime import datetime
import logging


class CrudDataBase:

    def __init__(self):
        try:

            self.conn = psycopg2.connect(
                database="users",
                user="Volodymyr",
                password="root",
                host="localhost"
            )

            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM users;")
        except(Exception, psycopg2.Error) as error:
            print("Something went wrong")

        def create_user(user_info: dict):
            self.cursor = self.conn.cursor()
            create_user_query = "INSERT INTO users (name, email, registration_time)" \
                                "VALUES (%(names)s, %(email)s, %(registration_time)s);"

            result = self.cursor.execute(create_user_query, user_info)

            self.conn.close()

        def read_user_info(_id: int):
            read_user_query = "SELECT _id " \
                              "FROM users WHERE id =%s, (_id,);"

            result = self.cursor.execute(read_user_query)
            result = self.cursor.fetchone()
            return result

        def update_user(new_info: dict, _id: int):
            update_user_query = "UPDATE users SET name = %(name)s, email = %(email)s, " \
                                "registration_time = %(registration_time)s WHERE id = %s;"
            self.conn.commit()
            self.cursor.execute(update_user_query, new_info)

        def delete_user(_id: int):
            delete_user_query = "DELETE FROM users WHERE id = %s;"

            self.cursor.execute(delete_user_query, _id)

        def create_cart(cart: dict):
            create_cart_query = "INSERT INTO cart (creation_time, user_id)" \
                                "VALUE (%(creating_time)s, %(user_id)s);"

            self.cursor.execute(create_cart_query, cart)

        def last_created_card(self):
            last_created_card_query = "SELECT id, name FROM users ORDER BY id DESC LIMIT 1"

            self.cursor.execute(last_created_card_query)
            return self.cursor.fetchone()[0]

        def update_cart(cart: dict):
            update_cart_query = "UPDATE users SET creating_time = %(creating_time)s, user_id = %(user_id)s" \
                                "WHERE id = %s;"

            self.cursor.execute(update_cart_query, cart)

        def read_cart(_id: int):
            read_cart_query = "SELECT _id " \
                              "FROM cart WHERE id =%s, (_id,);"

            self.cursor.execute(read_cart_query, _id)

        def delete_cart(_id: int):
            delete_cart_query = "DELETE FROM cart WHERE id = %s;"

            self.cursor.execute(delete_cart_query, _id)
            return self.cursor.fetchone()[0]
