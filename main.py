from fastapi import FastAPI, Path, Query, status
from fastapi.responses import HTMLResponse, JSONResponse
from typing import List
from variables import SYSTEM_CONFIG
from jwt_manajer import create_token
from models.Movie import Movie
from models.User import User
from data.movies import movies

app = FastAPI()
app.title: str = "My API"
app.version: str = "0.0.1"

@app.get("/", tags=["home"])
def message():
    return HTMLResponse(content="<h1>Welcome to my API</h1>", status_code=status.HTTP_200_OK)

@app.post("/login", tags=["auth"], response_model=dict, status_code=status.HTTP_200_OK)
def login(user: User):
    if user.email == SYSTEM_CONFIG["USER_EMAIL"] and user.password == SYSTEM_CONFIG["USER_PASSWORD"]:
        token: str = create_token({"email": user.email})
        return JSONResponse(content={"token": token}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"message": "Invalid credentials"}, status_code=status.HTTP_401_UNAUTHORIZED)

@app.get('/movies', tags=["movies"], response_model=List[Movie], status_code=status.HTTP_200_OK)
def message() -> List[Movie]:
    return JSONResponse(content={"data": [movie.model_dump() for movie in movies]}, status_code=status.HTTP_200_OK)

@app.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=status.HTTP_200_OK)
def get_movie(id: int = Path(ge=1, le=2000, description="The ID of the movie you want to get")) -> Movie:
    item = [i for i in movies if i.id == id]
    if len(item) > 0:
        return JSONResponse(content={"data": item[0].model_dump()}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"data": {}}, status_code=status.HTTP_404_NOT_FOUND)

@app.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies_by_category(category: str = Query(min_length=3, max_length=15, description="The category of the movies you want to get")) -> List[Movie]:
    item = [i for i in movies if (i.category == category)]
    if len(item) > 0:
        return JSONResponse(content={"data": [movie.model_dump() for movie in item]}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"data": []}, status_code=status.HTTP_404_NOT_FOUND)

@app.post('/movies', tags=['movies'], response_model=dict, status_code=status.HTTP_201_CREATED)
def add_movie(movie: Movie):
    movies.append(movie.model_dump())
    return JSONResponse(content={"message": "Movie added"}, status_code=status.HTTP_201_CREATED)

@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=status.HTTP_200_OK)
def update_movie(id: int, movie: Movie):
    for i in range(len(movies)):
        if movies[i].id == id:
            movies[i] = movie
            return JSONResponse(content={"message": "Movie updated"}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"message": "Movie not found"}, status_code=status.HTTP_404_NOT_FOUND)

@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=status.HTTP_200_OK)
def delete_movie(id: int):
    item = [i for i in movies if i.id == id]
    if len(item) > 0:
        movies.remove(item[0])
        return JSONResponse(content={"item": item[0], "message": "Movie deleted"}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"message": "Movie not found"}, status_code=status.HTTP_404_NOT_FOUND)