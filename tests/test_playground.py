"""
Tests for the Playground class
"""
from spicy_snake.playground import Playground
from unittest.mock import MagicMock
import random


def test_create():
    """creating a Playground object works"""
    p = Playground(10, 11)
    # after creating a Playground object it has the correct size attribute
    assert p.size == (10, 11)


def test_is_obstacle():
    """Check for obstacles on the playground"""
    p = Playground(5, 6)
    assert p.is_obstacle((3, 3)) is False
    assert p.is_obstacle((-1, -1)) is True
    assert p.is_obstacle((5, 6)) is True
    assert p.is_obstacle((0, 6)) is True
    assert p.is_obstacle((0, 0)) is True


def test_add_food():
    """food should be inside the Playground"""
    p = Playground(5, 6)
    p.add_food((3, 3))
    assert p.food == (3, 3)


def test_add_food_boundary():
    """Food cannot be added on obstacles"""
    p = Playground(5, 6)
    p.add_food((0, 0))
    assert p.food is None


def test_add_food_boundary_sequence():
    """Food is deleted if an invalid position is given"""
    p = Playground(5, 6)
    p.add_food((3, 3))
    assert p.food is not None
    p.add_food((0, 0))
    assert p.food is None


def test_add_random_food_mock():
    """Hijack the random function to produce predictable output"""
    p = Playground(5, 6)
    mm = MagicMock(return_value=4)
    random.randint = mm
    p.add_random_food()
    assert p.food == (4, 4)
    assert mm.call_count == 2
