import json
from src.entities.book import Book


class BookRepository:
  def insert(book: Book):
    with open("hospedes.data.json") as file:
      data = json.load(file)