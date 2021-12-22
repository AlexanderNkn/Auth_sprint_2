import uuid
from typing import Optional

from .base import BaseModel


class PersonName(BaseModel):
    id: uuid.UUID
    name: str


class Film(BaseModel):
    id: uuid.UUID
    imdb_rating: float
    genre: list[str]
    title: str
    description: str
    director: Optional[list[str]]
    actors_names: Optional[list[str]]
    writers_names: Optional[list[str]]
    actors: list[PersonName]
    writers: list[PersonName]
