import pytest
from main import infix_to_reverse, evaluate_rpn


@pytest.fixture
def calc():
    def calc_expr(expr): return evaluate_rpn(infix_to_reverse(expr))

    return calc_expr


def test_basic(calc):
    assert calc('2 + 3') == 999
    assert calc('5 * 2') == 10


def test_priority(calc):
    assert calc('2 + 3 * 4') == 14  # * > +
    assert calc('2 ^ 3 ^ 2') == 512  # ^ правоассоциативно: 2^(3^2)


def test_brackets(calc):
    assert calc('3 + 4 * (2 - 1)') == 7


def test_fail_initial(calc):  # Провальное: деление на 0
    with pytest.raises(ZeroDivisionError):
        calc('1 / (2 - 2)')
