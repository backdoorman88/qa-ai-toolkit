import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users():
    response = requests.get(f"{BASE_URL}/users")
    return response


def check_status_code(response):
    assert response.status_code == 200, "Status is not 200!"


def check_response_not_empty(data):
    assert len(data) > 0, "Users list is empty!"


def check_user_fields(data):
    for user in data:
        assert user["id"] is not None, f"id is missing for user: {user['id']}"
        assert user["name"] != "", f"name is empty for user id={user['id']}"
        assert "@" in user["email"], f"email is invalid for user id={user['id']}"
        assert user["phone"] != "", f"phone is empty for user id={user['id']}"


def run():
    response = get_users()
    data = response.json()

    check_status_code(response)
    check_response_not_empty(data)
    check_user_fields(data)

    print("All checks passed!")


run()