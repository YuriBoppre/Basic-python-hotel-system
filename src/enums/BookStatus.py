from enum import Enum

class BookStatus(Enum):
  RESERVED = 'R'  
  CANCELLED = 'C'
  ACTIVE = 'A'
  FINISHED = 'F'