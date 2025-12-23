from app import add

def test_add():
    assert add(2, 3) == 5

import os

username = os.getenv("USERNAME")
print(f"Running as {username}")
