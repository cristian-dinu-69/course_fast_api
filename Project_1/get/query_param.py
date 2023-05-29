from fastapi import FastAPI
app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
# working
@app.get("/books/")

async def read_categ_by_query(category:str):
    books_to_return =[]
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# working
@app.get("/books/{book_author}/")

async def read_categ_by_query(book_author:str,category:str):
    books_to_return =[]
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold():
            if book.get("category").casefold() == category.casefold():
                books_to_return.append(book)
    return books_to_return