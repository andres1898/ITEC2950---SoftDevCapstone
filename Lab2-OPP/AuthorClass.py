class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        return f'The author {self.name} has published: {self.books}'

    def publish(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            print(f'{book} already added')

def main():
    Lucero = Author('Lucero Fuentes')
    Lucero.publish("Your vivid memory")
    Lucero.publish("What you left behind")
    Lucero.publish("What you left behind")
    print(Lucero)

if __name__ == '__main__':
    main()