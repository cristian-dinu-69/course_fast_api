1. # Create a new API Endpoint that can fetch all books from a specific author 
# using either Path Parameters or Query Parameters.

from fastapi import Body,FastAPI
app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}


]

# {"title": "Title new","author":"Author New","category": "Category New"}
# get all books endpoint:

# @app.get("/books/read_all_books")
# async def read_all_book():
#     return BOOKS

# # post add a temporary book endpoint

# @app.post("/books/add_new_book")
# async def add_a_book(new_book=Body()):
#     BOOKS.append(new_book)

# # put - modify a book to books endpoint

# @app.put("/books/update_book")
# async def update_book(updated_book = Body()):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
#             BOOKS[i]= updated_book

# # delete the temporary book endpoint
# @app.delete("/books/delete/{book_title}")
# async def delete_book(book_title):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get("title").casefold() == book_title.casefold():
#             BOOKS.pop(i)
#             break

# get all books from a specific author or query_params

@app.get("/books/by_author")

async def read_all_books_by_author_query(author:str):
    books_to_return =[]
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


