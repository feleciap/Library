import json
import os
from typing import List, Union
from book import Book

DATA_FILE = "library.json"

class Library:
    def __init__(self):
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return [Book.from_dict(book) for book in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return[]
        
    def save_books(self) -> None:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4, ensure_ascii=False)

    def add_book(self, title: str, author: str, year: int) -> None:
        new_id = max((book.id for book in self.books), default=0) + 1
        self.books.append(Book(book_id= new_id, title=title, author=author, year=year))
        self.save_books()
        print(f"\nКнига с ID {new_id} успешно добавлена!\n")

    def remove_book(self, book_id: int) -> None:
        book = next((book for book in self.books if book.id == book_id), None)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"\nКнига с ID {book_id} успешно удалена!\n")
        else:
            print("\nОшибка: Книга с таким ID не найдена.\n")

    def search_book(self, query: Union[str, int], field: str) -> List[Book]:
        if field == "title":
            return [book for book in self.books if query.lower() in book.title.lower()]
        elif field == "author":
            return [book for book in self.books if query.lower() in book.author.lower()]
        elif field == "year":
            return [book for book in self.books if book.year == query]
        else:
            return []

    def display_books(self) -> None:
        if not self.books:
            print("\nБиблиотека пуста.\n") 
        else:
            print("\nСписок книг:\n")
            for book in self.books:
                status_text = "в наличии" if book.status else "выдана"
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {status_text}")

    def update_status(self, book_id: int, new_status: bool) -> None:
        book = next((book for book in self.books if book.id == book_id), None)
        if book:
            book.status = new_status
            self.save_books()
            status_text = "в наличии" if new_status else "выдана"
            print(f"\nСтатус книги с ID {book_id} успешно обновлён на '{status_text}'!\n")
        else:
            print("\nОшибка: Книга с таким ID не найдена.\n")
