from freezegun import freeze_time
from homework.flask.Amazon_killer import amazon_killer as app
import pytest


@pytest.fixture
def store_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


@freeze_time('2021-02-08 14:16:41')
def test_create_user(store_app):
    response = store_app.post(
        '/users',
        json={
            "name": "Illia",
            "email": "illia.sukonnik@gmail.com",
        })
    assert response.status_code == 201
    assert response.json == {
        "user_id": 1,
        "registration_timestamp": '2021-02-08T14:16:41'
    }
    user_id = response.json['user_id']

    response = store_app.get(f'/users/{user_id}')

    assert response.status_code == 200
    assert response.json == {
        "name": "Illia",
        "email": "illia.sukonnik@gmail.com",
        "user_id": user_id,
        "registration_timestamp": '2021-02-08T14:16:41',
    }

    response = store_app.put(
        "/users/1",
        json={
            "name": "Volodymyr",
            "email": "test@bekar.com"
        }
    )
    assert response.status_code == 200
    assert response.json == {
        "status": "success"
    }

    response = store_app.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json == {
        "status": "success"
    }


def test_get_user_no_such_user(store_app):
    response = store_app.get('/users/2')

    assert response.status_code == 404
    assert response.json == {
        "error": "no such user with id 1"
    }


@freeze_time('2021-02-08 14:16:41')
def test_create_cart(store_app):
    response = store_app.post(
        "/carts/1",
        json={
            "user_id": 1,
            "products": [
                {
                    "product": "Book: how to stop be boring",
                    "price": 500,
                },
                {
                    "product": "fireworks",
                    "price": 1500,
                }

            ]
        }
    )
    assert response.status_code == 201
    assert response.json == {
        "cart_id": 1,
        "creating_time": "2021-02-08 14:16:41"
    }
    cart_id = response.json["cart_id"]

    response = store_app.get(f"/carts/{cart_id}")
    assert response.status_code == 200
    assert response.json == {
        "user_id": 1,
        "creation_time": '2021-02-08T14:16:41.892824',
        "products": [
            {
                "product": 'Book: how to stop be boring',
                "price": 500,
            },
            {
                "product": 'fireworks',
                "price": 1500,
            }
        ]
    }

    response = store_app.put(
        "/carts/1",
        json={
            "user_id": 1,
            "products": [
                {
                    "product": 'fireworks',
                    "price": 1500,
                }
            ]
        }
    )

    assert response.status_code == 200
    assert response.json == {
        "status": "success"
    }

    response = store_app.delete(f"/carts/{cart_id}")
    assert response.status_code == 200
    assert response.json == {
        "status": "success"
    }


@freeze_time('2021-02-08 14:16:41')
def test_get_no_such_cart(store_app):
    response = store_app.get("/cart/5")
    assert response.status_code == 404
    assert response.json == {
        "error": "no such cart with id 1"
    }
