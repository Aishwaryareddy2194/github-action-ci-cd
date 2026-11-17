
from app import login


def test_login_success():
    assert login("admin", "1234") == "Welcome! Login successful"


def test_login_failure():
    assert login("user", "wrong") == "Sorry! Invalid username or password"
