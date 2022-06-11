import pytest
from src.entities.option import Option

def test_should_raise_exception_because_value_is_greater_than_upper_limit():
  with pytest.raises(ValueError):
    Option("7")
