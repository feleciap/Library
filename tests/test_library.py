import pytest
import os
import json
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.library import Library, Book

@pytest.fixture
def test_data_file(tmp_path):
    # Создаем временный файл для тестов
    return tmp_path / "test_library.json"

@pytest.fixture
def setup_library(test_data_file):
    # Создаем библиотеку с тестовыми данными
    library = Library()
    library.file_path = test_data_file  # Устанавливаем путь к временно создаваемому файлу
    library.books = [
        Book(book_id=1, title="Book1", author="Author A", year=2001, status=True),
        Book(book_id=2, title="Book2", author="Author B", year=2002, status=False)
    ]
    library.save_books()  # Сохраняем данные в тестовый файл
    return library

# Тесты для методов библиотеки
def test_load_books(setup_library):
    library = setup_library
    assert len(library.books) == 2
    assert library.books[0].title == "Book1"

def test_add_book(setup_library):
    library = setup_library
    library.add_book("New Book", "New Author", 2015)
    assert len(library.books) == 3
    assert library.books[-1].title == "New Book"

def test_remove_book(setup_library):
    library = setup_library
    library.remove_book(1)
    assert len(library.books) == 1
    assert library.books[0].id != 1

def test_seach_book_by_title(setup_library):
    library = setup_library
    results = library.search_book("Book1", "title")
    assert len(results) == 1
    assert results[0].author == "Author A"

def test_seach_book_by_author(setup_library):
    library = setup_library
    results = library.search_book("Author B", "author")
    assert len(results) == 1
    assert results[0].title == "Book2"

def test_update_status(setup_library):
    library = setup_library
    library.update_status(2, True)
    assert library.books[1].status is True

def test_save_books(setup_library, test_data_file):
    library = setup_library
    library.add_book("Book5", "Author K", 2024)
    library.save_books()

    # Проверяем, что книга была записана в файл
    with open(test_data_file, "r", encoding="utf-8") as f:
        data = f.read()
    assert "Book5" in data  # Проверяем, что книга "Book5" присутствует в данных

def test_display_books(capsys, setup_library):
    library = setup_library
    library.display_books()
    captured = capsys.readouterr()
    assert "Book1" in captured.out
    assert "Book2" in captured.out
