import pytest
from src.app import greet


def test_greet():
    assert greet("Rida") == "Hello, Rida!"


def test_greet_removes_extra_spaces():
    assert greet("  Gitflow  ") == "Hello, Gitflow!"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ")
from src.app import goodbye


def test_goodbye():
    assert goodbye("Rida") == "Goodbye, Rida!"