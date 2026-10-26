from app import greet


def test_greet():
    assert greet() == "Hello! Application is running successfully."