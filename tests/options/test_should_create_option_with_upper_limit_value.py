from src.entities.option import Option

def test_should_create_option_with_upper_limit_value():
  option = Option("6")
  assert option.value == 6