from functools import reduce
from decimal import Decimal
from uuid import uuid4
from src.enums.BookStatus import BookStatus
from src.enums.RoomType import RoomType

class Book:
  def __init__(self, name, cpf, number_of_days, number_of_people, room_type, id = uuid4()):
    self.id = id
    self.name = name
    self.cpf = cpf
    self.number_of_days = number_of_days
    self.number_of_people = number_of_people
    self.room_type = room_type
    self._verify_required_fields()
    
    self.status = BookStatus.RESERVED
    self.value = self.calculate_value()
    
  def calculate_value(self):
    if self.room_type == RoomType.STANDARD:
      self.value = Decimal(f"{self.number_of_days * self.number_of_people * 100:.2f}")
    elif self.room_type == RoomType.DELUXE:
      self.value = Decimal(f"{self.number_of_days * self.number_of_people * 200:.2f}")
    else:
      self.value = Decimal(f"{self.number_of_days * self.number_of_people * 300:.2f}")
      
  def serialize(self):
    ...
      
  def _verify_required_fields(self):
    errors = []

    if self.name == None:
      errors.append("Nome é obrigatório") 
    if self.cpf == None: 
      errors.append("CPF é obrigatório") 
    if self.number_of_days == None:
      errors.append("Número de dias é obrigatório")
    if self.number_of_people == None:
      errors.append("Número de pessoas é obrigatório")
    if self.room_type == None:
      errors.append("Tipo de quarto é obrigatório")

    if errors.count > 0:
      error_message = str(reduce(lambda x, y: f"{x}, {y}", errors))
      raise ValueError(error_message)
    
  def check_in(self):
    self.status = BookStatus.ACTIVE
    
  def check_out(self):
    self.status = BookStatus.FINISHED
    
  def cancel(self):
    self.status = BookStatus.CANCELLED