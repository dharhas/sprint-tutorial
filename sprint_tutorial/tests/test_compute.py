""" Tests for the compute module
"""

from sprint_tutorial.compute import my_sum
import pytest

def test_my_sum():
    assert my_sum(0, 0) == 0
    assert my_sum(3, 0) == 3
