import requests

#get books tittles
all_books_url = "http://127.0.0.1:5000/api/books"
response_book_title = requests.get(all_books_url).json()
print(response_book_title)

#get books count
book_count_url = "http://127.0.0.1:5000/api/book_count"
new_books_url = "http://127.0.0.1:5000/api/new_books"
#response_book_count = requests.get(book_count_url).json()
#print(response_book_count)

#add a new book
new_book_info = {'name': 'Othello'}
response_post = requests.post(new_books_url, data=new_book_info)
print(response_post.text)
print(response_post.status_code) # 2xx code is expected to successful