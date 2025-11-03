import pytest
from calculator import Calculator

c1 = Calculator(1, 2)
c2 = Calculator(4, 2334566565)
c3 = Calculator(-53243, -0.000004)
c4 = Calculator(2, 1)
c5 = Calculator(2, 0)


@pytest.mark.parametrize(
    "c, result", [(c1, 3), (c2, 2334566569), (c3, -53243.000004), (c4, 3), (c5, 2)]
)
def test_add(c: Calculator, result: int):
    assert pytest.approx(c.sum()) == result


@pytest.mark.parametrize(
    "c, result", [(c1, -1), (c2, -2334566561), (c3, -53242.999996), (c4, 1), (c5, 2)]
)
def test_subtract(c, result):
    assert pytest.approx(c.subtract()) == result


@pytest.mark.parametrize("c, result", [(c1, 2), (c2, 9338266260), (c4, 2), (c5, 0)])
def test_multiply(c, result):
    assert pytest.approx(c.multiply()) == result


@pytest.mark.parametrize(
    "c, result",
    [
        (c1, 0.5),
        (c4, 2),
        (c5, None),
    ],
)
def test_divide(c, result):
    assert pytest.approx(c.divide()) == result
