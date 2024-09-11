from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    id: int
    title: str
    body: str

@app.get('/')
def home() -> dict[str, str]:
    return {'data': 'hello'}


@app.get('/contacts')
def contacts() -> int:
    return 34


posts = [
    {'id': 1, 'title': 'News 1', 'body': 'Text 1'},
    {'id': 2, 'title': 'News 2', 'body': 'Text 2'},
    {'id': 3, 'title': 'News 3', 'body': 'Text 3'},
]


@app.get('/items')
async def items() -> list:
    return posts


@app.get('/items/{id}')
def items(id: int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post

    raise HTTPException(status_code=404, detail='Post not found')


@app.get('/search')
def search(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return post

        raise HTTPException(status_code=404, detail='Post not found')
    else:
        return {'data': 'No post id provided'}