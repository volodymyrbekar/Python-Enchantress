import pytest
import datetime
import psycopg2
from homework.sql_practice.HW_sql import CrudDataBase


@pytest.fixture()
def test_fixture():
    test_fixture = CrudDataBase()
    yield
    test_fixture.cursor.close()
    test_fixture.conn.close()


worng_user = {
    "name": "test",
    "email": "aaa@gmail.com",
    "registration_time": "1111111"
}


class PositiveTESTS:

    def test_crud_user(self, test_fixture):
        user_info = {"name": "Volodymyr", "email": "test@gmail.com", "registration_time": "2021-02-04 14:48:47"}

        test_fixture.create_user(user_info)

        user_id = test_fixture.read_user_info()

        update_user_info = {"id": user_id, "name": "Vova", "email": "test333@gmail.com",
                            "registration_time": "2021-02-05 15:33:33"}

        assert test_fixture.read_user_info(user_info) == ("Volodymyr", "test@gmail.com",
                                                          datetime.datetime(2021, 2, 4, 14, 48, 47))

        test_fixture.update_user(update_user_info)
        assert test_fixture.read_user_info(user_id) == (user_id, "Vova", "test333@gmail.com",
                                                        datetime.datetime(2021, 2, 4, 15, 33, 33))

        test_fixture.delete_user(user_id)
        assert test_fixture.read_user_info(user_id) is None

    def test_cart_crud(self, text_fixture):
        user_info = {"name": "VVV", "email": "nixtest@gmail.com", "registration_time": "2021-02-06 11:11:00"}
        test_fixture.create_cart(user_info)
        user_id = text_fixture.last_created_card()

        new_cart = {"creating_time": "2021-02-05 12:12:00", "user_id": user_id,
                    "cart_details": [{"price": 200, "product": "mandarin"}]}

        text_fixture.create_cart(new_cart)
        cart_id = text_fixture.last_created_card()

        assert text_fixture.read_cart(cart_id) == [(datetime.datetime(2021, 2, 5, 12, 12, ), 200, "mandarin")]

        text_fixture.delete_cart(cart_id)
        assert text_fixture.read_cart(cart_id) == []


class NegativeTESTS:

    def test_crud_user(self, test_fixture):
        wrong_user_id = 101
        pytest.raises(psycopg2.Error, lambda: test_fixture.create_user(worng_user))

        assert test_fixture.read_user_info(worng_user) is None

        update_wrong_user_info = {"id": 35, "name": "BBC", "email": "bbc@bbc.com",
                                  "registration_time": "1241u41"}

        pytest.raises(psycopg2.Error, lambda: test_fixture.read_user_info(update_wrong_user_info))

        assert test_fixture.delete_user(wrong_user_id) is None

    def test_crud_cart(self, text_fixture):
        wrong_user_id = 100
        new_cart = {"creating_time": "2021-02-05 12:12:00", "user_id": wrong_user_id,
                    "cart_details": [{"price": 200, "product": "mandarin"}]}

        updated_cart = {"id": 1, "creating_time": "2021-02-05 12:12:00", "user_id": wrong_user_id,
                        "cart_details": [{"price": 200, "product": "mandarin"}]}

        pytest.raises(psycopg2.Error, lambda: text_fixture.create_cart(new_cart))

        assert text_fixture.read_cart(wrong_user_id) == []

        pytest.raises(psycopg2.Error, lambda: text_fixture.read_cart(updated_cart))

        assert test_fixture.delete_cart(wrong_user_id) is None
