from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15, default="No title")
    overview: str = Field(min_length=15, max_length=100, default="No overview")
    year: int = Field(gt=1900, le=2022, default=2022)
    rating: float
    category: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Avatar",
                "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
                "year": 2009,
                "rating": 7.8,
                "category": "Acción"
            }
        }