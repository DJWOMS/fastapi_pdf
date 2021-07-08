from pydantic import BaseModel


class Doc(BaseModel):
    title: str
    text: str
    author: str


class DocOut(Doc):
    id: int
