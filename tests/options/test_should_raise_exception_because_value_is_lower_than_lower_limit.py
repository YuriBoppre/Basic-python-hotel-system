import pytest
from src.entities.option import Option

def test_should_raise_exception_because_value_is_lower_than_lower_limit():
  with pytest.raises(ValueError):
    Option("0")
