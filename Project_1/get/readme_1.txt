# 1. 

from fastapi import FastAPI
# read = get
app = FastAPI()

@app.get("api-endpoint")
async def first_api():
    return {"message":"Hello Eric"}

# from terminal :
# activate environment with
# source fastapi_env/bin/activate

# then run:
# uvicorn books_1:app --reload 
# go to http://127.0.0.1:8000/api-endpoint
# you should get the following message :
# {"message":"Hello Eric"}

# save books_1.py

# 2. 
# add BOOKS
BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

comment this :

# @app.get("api-endpoint")
# async def first_api():
#    return {"message":"Hello Eric"}

add/replace the code with :

# @app.get("books")
# async def read_all_books():
#    return BOOKS

# save books_1.py 

# reload the web page - changing api-endpoint with books

