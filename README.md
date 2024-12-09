# Library Management System

### Описание проекта

Это приложение для управления библиотекой, реализованное на Python. Проект предоставляет функционал для добавления, удаления, поиска и обновления статуса книг, а также для сохранения и загрузки информации о книгах из JSON-файла.

### Основные возможности

+ Добавление книг с информацией о названии, авторе и году издания.

+ Удаление книг по ID.

+ Поиск книг по названию или автору.

+ Обновление статуса книги (в наличии/выдана).

+ Сохранение данных о книгах в JSON-файл.

+ Загрузка данных о книгах из JSON-файла.

+ Отображение всех книг в библиотеке.

## Установка и запуск

### Шаг 1: Клонирование репозитория

Склонируйте репозиторий на локальную машину:

`git clone git@github.com:feleciap/Library.git`

### Шаг 2: Запуск программы

Для запуска программы выполните:

`python3 main.py`

## Тестирование

Проект содержит модульные тесты, написанные с использованием `pytest`.

### Запуск тестов

Для запуска всех тестов выполните:

`pytest tests/test_library.py`

## Структура проекта

Librar/  
├── src/  
│   ├── library.py       
│   ├── book.py  
│   └── main.py           
├── tests/  
│   └── test_library.py  
└── README.md            

## Как использовать

1. Добавьте книги в библиотеку с помощью метода add_book().

2. Используйте метод search_book() для поиска книг по названию или автору.

3. Обновите статус книги с помощью метода update_status().

4. Сохраните данные в файл с помощью метода save_books().

5. Загрузите данные из файла с помощью метода load_books().


