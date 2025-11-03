import pytest
from calculator import Calculator

# It would be better to create separate test functions for ints (using assert) and floats (pytest.approx)


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
def test_add(a: float, b: float, result: float):
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
def test_subtract(a: float, b: float, result: float):
    c = Calculator(a, b)
    assert pytest.approx(c.subtract()) == result


@pytest.mark.parametrize(
    "a, b, result",
    [(1, 2, 2), (4, 2334566565, 9338266260), (-0.1, -0.2, 0.02), (2, 1, 2), (2, 0, 0)],
)
def test_multiply(a: float, b: float, result: float):
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
def test_divide(a: float, b: float, result: float):
    c = Calculator(a, b)
    assert pytest.approx(c.divide()) == result


@pytest.mark.parametrize("a,b", [(2, -0.0), (2, 0)])
def test_divide_by_zero_raise_error(a: float, b: float):
    c = Calculator(a, b)
    with pytest.raises(ZeroDivisionError):
        c.divide()
