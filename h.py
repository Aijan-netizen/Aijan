class Book:
    def __init__(self, title, author, ISBN=None, price=None):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price

    def read(self):
        print(f"The book '{self.title}' by {self.author}.")

    def info(self):
        print(f"Book title={self.title}, author={self.author}, ISBN={self.ISBN}, price={self.price}")

if __name__ == "__main__":
    book1 = Book("Death Souls", "Nikolai Gogol", "978-0140448078", 15)
    book2 = Book("Cranes Fly Early", "Chyngyz Aitmatov")

    book1.info()
    book2.info()

    book1.read()