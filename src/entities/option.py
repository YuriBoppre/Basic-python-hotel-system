class Option:
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

