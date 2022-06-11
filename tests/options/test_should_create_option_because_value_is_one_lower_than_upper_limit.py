from src.entities.option import Option

def test_should_create_option_because_value_is_one_lower_than_upper_limit():
  option = Option("5")
  assert option.value == 5
