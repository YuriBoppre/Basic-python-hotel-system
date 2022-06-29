class Cpf:
    def __init__(self, value: int | str):
        self.value = value
        
    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, new_value: int | str):
        start = 1
        end = 6
        valid_options = [x for x in range(start, end + 1)] + [str(x) for x in range(start, end + 1)]
        if new_value not in valid_options:
            raise ValueError("O valor digitado deve ser uma opção válida")
        self.__value = int(new_value)

    def __verify_verifications_digits(self, cpf: str):
        first_is_valid = False
        cpf_list = list(map(lambda x: int(x)))
        
        value = 0
        for number in range(2, 11):
            index = (number + 1) * (-1)
            value += cpf_list[index] * number
        
        rest = value % 11
        
        if rest == 0 or rest == 1:
            if cpf_list[-2] == 0:
                first_is_valid = True
        elif rest >= 2 and rest <= 10:
            if cpf_list[-2] == 11 - rest:
                first_is_valid = True
        
        # second digit
        second_is_valid = False
        
        value = 0
        for number in range(2, 12):
            index = (number) * (-1)
            value += cpf_list[index] * number
        
        rest = value % 11
        
        if rest == 0 or rest == 1:
            if cpf_list[-1] == 0:
                second_is_valid = True
        elif rest >= 2 and rest <= 10:
            if cpf_list[-1] == 11 - rest:
                second_is_valid = True
                
        if first_is_valid and second_is_valid:
            return True

        return False

    def __verify_second_verification_digit(self, digit: int):
        ...
