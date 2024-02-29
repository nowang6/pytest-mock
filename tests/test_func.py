import pytest
from src.func import Caculator
from unittest.mock import MagicMock


def test_add():
    c = Caculator()
    assert c.add(4, 8) == 12


def test_subtract():
    c = Caculator()
    assert c.subtract(3, 6) == -3


def test_multiply():
    c = Caculator()
    assert c.multiply(4, 5) == 20


def test_divide():
    c = Caculator()
    assert c.divide(56, 8) == 7


def test_dollar2rmb_with_mock():
    c = Caculator()
    mock = MagicMock()
    mock.get_rate.return_value = 7
    c.rater = mock
    assert c.dollar2rmb(1) == 7


def test_dollar2rmb_without_mock():
    c = Caculator()
    assert c.dollar2rmb(1) == 6


@pytest.mark.parametrize("a, b, c", [(10, 20, 30), (20, 40, 60), (11, 22, 33)])
def test_add_ddt(a, b, c):
    caculator = Caculator()
    res = caculator.add(a, b)
    assert res == c