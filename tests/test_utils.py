
from files.utils import add
import pytest


@pytest.mark.parametrize('x, y, result', [
    (10, 10, 20),
    (5, 5, 10),
    (6, 6, 12),
    (6, 7, 13)
])
def test_add(x, y, result):
    assert add(x, y) == result # #assert - whatevere we are testing, it is supposed to be true
