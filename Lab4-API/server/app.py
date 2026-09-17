from flask import Flask, request, jsonify

app = Flask(__name__)

print(__name__)

books_published = ['1984', 'Automate the Boring Stuff']

#GET requests
@app.route('/api/books')
def all_books():
    return jsonify(books_published)

@app.route('/api/book_count')
def book_count():
    return jsonify({"total books: ": len(books_published)})

# PUSH request
@app.route('/api/new_books', methods=['POST'])
def add_book():
    new_book_data = request.form #JSON data sent in the body of a request
    name = new_book_data.get('name')
    if name is None:
        return "error: Please enter a name", 400 #bad request
    # check for duplicate
    if name in books_published:
        return "error: Book already exists", 400 #bad request
    else:
        # add the book
        books_published.append(name)
        return 'ok', 201 #request complete


if __name__ == '__main__':
    app.run(debug=True)