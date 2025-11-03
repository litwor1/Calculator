import pytest
from calculator import Calculator

# c1 = Calculator(1, 2)
# c2 = Calculator(4, 2334566565)
# c3 = Calculator(-2334566565, -0.000004)
# c4 = Calculator(2, 1)
# c5 = Calculator(2, 0)


@pytest.mark.parametrize(
    "a, b, result",
    [
        (1, 2, 3),
        (4, 2334566565, 2334566569),
        (-0.1, -0.2, -0.3),
        (2, 1, 3),
        (2, 0, 2),
    ],
)
def test_add(a: int, b: int, result: int):
    c = Calculator(a, b)
    assert pytest.approx(c.sum()) == result


@pytest.mark.parametrize(
    "a, b, result",
    [
        (1, 2, -1),
        (4, 2334566565, -2334566561),
        (-0.1, -0.2, 0.1),
        (2, 1, 1),
        (2, 0, 2),
    ],
)
def test_subtract(a: int, b: int, result):
    c = Calculator(a, b)
    assert pytest.approx(c.subtract()) == result


@pytest.mark.parametrize(
    "a, b, result",
    [(1, 2, 2), (4, 2334566565, 9338266260), (-0.1, -0.2, 0.02), (2, 1, 2), (2, 0, 0)],
)
def test_multiply(a: int, b: int, result):
    c = Calculator(a, b)
    assert pytest.approx(c.multiply()) == result


@pytest.mark.parametrize(
    "a,b, result",
    [
        (1, 2, 0.5),
        (2, 1, 2),
        (-0.1, -0.2, 0.5),
    ],
)
def test_divide(a: int, b: int, result):
    c = Calculator(a, b)
    assert pytest.approx(c.divide()) == result


def test_divide_by_zero():
    c = Calculator(2, 0)
    with pytest.raises(ZeroDivisionError):
        c.divide()
