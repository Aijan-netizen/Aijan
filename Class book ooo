class Book:
    def __init__(self, title, author, ISBN=None, price=None):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price

    def read(self):
        print(f'Reading the book "{self.title}" by {self.author}.')

    def info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        if self.ISBN:
            print(f'ISBN: {self.ISBN}')
        if self.price is not None:
            print(f'Price: ${self.price:.2f}')
        print()  # Adds an empty line for better readability

if __name__ == '__main__':
    book1 = Book('Dead Souls', 'Nikolai Gogol', '978-0140448078', 15)
    book2 = Book('Cranes Fly Early', 'Chyngyz Aitmatov')
    book1.info()
    book2.info()
    book1.read() 
