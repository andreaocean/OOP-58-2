class LibraryBook:
    def __init__(self, title, secret_code):
        self.title = title              # открытый атрибут
        self._is_taken = False           # защищённый атрибут
        self.__secret_code = secret_code # приватный атрибут

    def take_book(self, code):
        if self._is_taken:
            print(f"Книга '{self.title}' уже взята.")
        elif code == self.__secret_code:
            self._is_taken = True
            print(f"Вы взяли книгу '{self.title}'.")
        else:
            print("Неверный секретный код! Книга не выдана.")

    def return_book(self):
        if self._is_taken:
            self._is_taken = False
            print(f"Книга '{self.title}' возвращена.")
        else:
            print(f"Книга '{self.title}' не была взята.")

book = LibraryBook("Манас", "12345")

book.take_book("00000")  # Неверный код
book.take_book("12345")  # Берём книгу
book.take_book("12345")  # Уже взята
book.return_book()       # Возвращаем книгу





