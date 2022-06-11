from src.entities.option import Option

def test_should_create_option_with_lower_limit_value():
  option = Option("1")
  assert option.value == 1