import pytest
from calculator import Calculator

c1 = Calculator(1, 2)
c2 = Calculator(4, 2334566565)
c3 = Calculator(-53243, -0.000004)
c4 = Calculator(2, 1)


@pytest.mark.parametrize("c, result",
                         [(c1, 3),
                          (c2, 2334566569),
                          (c3, -53243.000004),
                          (c4, 3)
                          ])
def test_add(c, result):
    assert c.sum() == result


@pytest.mark.parametrize("c, result",
                         [(c1, -1),
                          (c2, -2334566561),
                          (c3, -53242.999996),
                          (c4, 1)
                          ])
def test_subtract(c, result):
    assert c.subtract() == result


@pytest.mark.parametrize("c, result",
                         [(c1, 0.5),
                          (c4, 2)
                          ])
def test_divide(c, result):
    assert c.divide() == result
