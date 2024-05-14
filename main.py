from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models.Movie import Movie
from data.movies import movies

app = FastAPI()
app.title: str = "My API"
app.version: str = "0.0.1"

@app.get("/", tags=["home"])
def message():
    return HTMLResponse(content="<h1>Welcome to my API</h1>", status_code=200)

@app.get('/movies', tags=["movies"])
def message():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    item = [i for i in movies if i.id == id]
    return item

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    item = [i for i in movies if (i.category == category and i.year  == year)]
    return item

@app.post('/movies', tags=['movies'])
def add_movie(movie: Movie):
    movies.append(movie)
    return movie

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    item = [i for i in movies if i.id == id]
    if item[0]:
        item[0] = movie
    return movie

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    item = [i for i in movies if i.id == id]
    if len(item) > 0:
        movies.remove(item[0])
        return {"item": item[0], "message": "Item deleted", "status_code": 200}
    return {"message": "Item not found", "status_code": 404}