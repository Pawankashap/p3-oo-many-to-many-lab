class Author:
    all = []

    def __init__(self, name):
        self.name = name

    def contracts(self):
        contracts_list = [
            contract for contract in Contract.all if contract.author == self
        ]
        return contracts_list

    def books(self):
        books_list = [
            contract.book for contract in Contract.all if contract.author == self
        ]
        return books_list

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        total = sum(
            contract.royalties for contract in Contract.all if contract.author == self
        )
        return total


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        contracts_list = [
            contract for contract in Contract.all if contract.book == self
        ]
        return contracts_list

    def authors(self):
        authors_list = [
            contract.author for contract in Contract.all if contract.book == self
        ]
        return authors_list


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of the Author Class.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("Book must be an instance of the Book Class.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("Date must be of type string.")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise TypeError("Royalties must be of type int.")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls):
        sorted_contracts = sorted(Contract.all, key=lambda contract: contract.date)
        return sorted_contracts