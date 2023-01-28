import pytest
from utils import arrs


@pytest.fixture
def col():
    return [1, 2, 3]


def test_get(col):
    assert arrs.get(col, 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice(col):
    assert arrs.my_slice(col, 0, 2) == [1, 2]
    assert arrs.my_slice(col, 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(col, -3, -1) == [1, 2]
    assert arrs.my_slice(col, -5) == [1, 2, 3]
