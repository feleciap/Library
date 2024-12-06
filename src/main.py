from library import Library

def main():
    library = Library()

    while True:
        print("""
Меню:
1. Добавить книгу
2. Удалить книгу
3. Найти книгу
4. Показать все книги
5. Изменить статус книги
q. Выход 
""")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            library.add_book(title, author, year)

        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                if not any(book.id == book_id for book in library.books):
                    print("\nОшибка: Книга с таким ID не найдена.\n")
                else:
                    library.remove_book(book_id)
            except ValueError:
                print("\nОшибка: ID книги должен быть числом.\n")

        elif choice == "3":
            field = input("По какому полю искать? (title/author/year): ").strip().lower()
            query = input("Введите значение для поиска: ")
            if field == "year":
                query = int(query)
            results = library.search_book(query, field)
            if results:
                print("\nНайденные книги:\n")
                for book in results:
                    status_text = "в наличии" if book.status else "выдана"
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {status_text}")
            else:
                print("\nКниги не найдены.\n")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги для изменения статуса: "))
                new_status_input = input("Введите новый статус (в наличии/выдана): ").strip()
                if new_status_input == "в наличии":
                    new_status = True
                elif new_status_input == "выдана":
                    new_status = False
                else:
                    print("\nОшибка: Неверный статус.\n")
                    continue
                library.update_status(book_id, new_status)
            except ValueError:
                print("\nОшибка: ID книги должен быть числом.\n")

        elif choice == "q":
            print("\nВыход из программы.\n")
            break

        else:
            print("\nОшибка: Неверный выбор.\n")
                
if __name__ == "__main__":
    main()