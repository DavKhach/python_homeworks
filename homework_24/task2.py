class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        if price >= 10:
            self.__price = price
        else:
            print("Price can't be below 10. Setting to 10")
            self.__price = 10


    title = property(get_title, set_title)
    author = property(get_author, set_author)
    price = property(get_price, set_price)


book = Book("War and Peace", "Lev Tolstoy", 20)
print(book.title)
print(book.author)
print(book.price)


book.price = 5
print(book.price)
