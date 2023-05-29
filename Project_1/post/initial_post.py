from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# read = get

# @app.get("/api-endpoint")
# async def first_api():
#     return {"message": "Hello Eric"}


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/books/create_book")

async def create_book(new_book = Body()):
    BOOKS.append(new_book)

# {"title": "New Title","author":"New Author","category": "New category"}