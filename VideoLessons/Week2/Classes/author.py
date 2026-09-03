class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, tittle):
        self.books.append(tittle)

    def __str__(self):
        # consist way
        # books_list = ', '.join(self.books) or 'No books'
        # return f'{Author}. Books published: {book_list}'
        if self.books:
            books_list = ', '.join(self.books)  # concatenate the elements by a ','
            return f'The author {self.name} has {len(self.books)} books.\n {books_list}'
        else:
            return f'{self.name}, no books published'


Lorenzo = Author('Lorenzo')

print(Lorenzo)

Lorenzo.publish("Book1")
print(Lorenzo)

Roberto = Author('Roberto')
print(Roberto)
