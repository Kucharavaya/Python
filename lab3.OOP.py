"""
Создайте класс и поля соответствующему вашему варианту
(поля статические и динамические). Создайте три метода
(класса, объекта и статический). Выберете поле или
метод для реализации инкапсуляции. Пропишите запись и
считывание (get, set) инкапсулированных полей.

-------------------------------Вариант 1------------------------------------------

Kласс Book: id, Название, Автор (ы), Издательство,
Год издания, Количество страниц, Цена, Тип переплета.
Функции-члены реализуют запись и считывание полей (проверка корректности).
Создать список объектов. Вывести:
a)	список книг заданного автора;
б) список книг, выпущенных после заданного года

"""


class Book:

    def __init__(self, id, title, author, publisher, year, pages, price, binding_type):
        self.__id = id                           # id
        self.__title = title                     # Название
        self.__author = author                   # Автор(ы)
        self.__publisher = publisher             # Издательство
        self.__year = year                       # Год издания
        self.__pages = pages                     # Количество страниц
        self.__price = price                     # Цена
        self.__binding_type = binding_type       # Тип переплета

    # Book.books.append(self)

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher

    def get_year(self):
        return self.__year

    def get_pages(self):
        return self.__pages

    def get_price(self):
        return self.__price

    def get_binding_type(self):
        return self.__binding_type

    def set_id(self, id):
        self.__id = id

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def set_year(self, year):
        self.__year = year

    def set_pages(self, pages):
        self.__pages = pages

    def set_price(self, price):
        self.__price = price

    def set_binding_type(self, binding_type):
        self.__binding_type = binding_type


    def PrintInfo(self):
        print(f"ID {self.__id}   "
              f"Название: {self.__title}   "
              f"Автор(ы): {self.__author}   "
              f"Издательство {self.__publisher}   "
              f"Год издания {self.__year}   "
              f"Количество страниц {self.__pages}   "
              f"Цена {self.__price}  "
              f"Тип переплета {self.__binding_type}")
    @staticmethod
    def books_after_year(year):
        return [book for book in books if book.__year >= year]


    @classmethod
    def list_books_author(cls, author):
        return [book for book in books if author in book.__author]


# создание списка объектов Book
books = [
        Book(1, "Начинаем программировать на Python", "Тони Гэддис", "издатель", 2022, 1000, 25.00, "Твердый переплет"),
        Book(2, "Учимся программировать с примерами на Python", "Эрик Фримен", "издатель", 2020, 2000, 12.56,
             "Твердый переплет"),
        Book(3, "Война и мир.", "Лев Толстой", "Лексика", 1996, 361, 16.99, "Твердый переплет"),
        Book(4, "Лолита", "Владимир Набоков", "Olympia Press", 1995, 156, 3.99, "Мягкий переплет"),
        Book(5, "Путешествия Гулливера", "Джонатан Свифт", "Olympia Press", 2023, 156, 13.59, "Мягкий переплет")]


print("Список всех имеющихся книг: ")
for book in books:
    book.PrintInfo()

# Вывод автора если он прописан в коде  "Лев Толстой"
# print("\na)	список книг заданного автора:\n")
# for book in Book.list_books_author("Лев Толстой"):
#     book.PrintInfo()

# Вывод автора при вводе с клавиатуры
print("\na)	список книг заданного автора:\n")
find_author = input("Введите кого будем искать?")
for book in Book.list_books_author(find_author):
    book.PrintInfo()

# Вывод книг после заданного года "2000"
print("\nб) список книг, выпущенных после заданного года: \n")
for book in Book.books_after_year(2000):
    book.PrintInfo()







