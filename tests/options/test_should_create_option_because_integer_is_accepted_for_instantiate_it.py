from src.entities.option import Option

def test_should_create_option_because_integer_is_accepted_for_instantiate_it():
  option = Option(1)
  assert option.value == 1
