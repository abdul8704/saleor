import pytest


@pytest.mark.parametrize("value", [1, 2, 3])
def test_autodocs_probe(value):
    assert value > 0
