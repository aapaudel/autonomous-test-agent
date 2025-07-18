class Book:
    def __init__(self, title: str, author: str, copies: int):
        self.title = title
        self.author = author
        self.copies = copies

    def is_available(self) -> bool:
        return self.copies > 0

    def borrow(self):
        if self.copies <= 0:
            raise ValueError("No copies available")
        self.copies -= 1

    def return_book(self):
        self.copies += 1


class LibrarySystem:
    def __init__(self):
        self.catalog: dict[str, Book] = {}

    def add_book(self, title: str, author: str, copies: int):
        if title in self.catalog:
            raise ValueError("Book already exists")
        self.catalog[title] = Book(title, author, copies)

    def borrow_book(self, title: str):
        if title not in self.catalog:
            raise KeyError("Book not found")
        self.catalog[title].borrow()

    def return_book(self, title: str):
        if title not in self.catalog:
            raise KeyError("Book not found")
        self.catalog[title].return_book()

    def available_books(self) -> list[str]:
        return [title for title, book in self.catalog.items() if book.is_available()]
