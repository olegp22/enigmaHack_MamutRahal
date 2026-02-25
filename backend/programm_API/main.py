from schema import User, UserCreate
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

app = FastAPI()

origins = [
    'https://localhost:'
]

app.middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post('/user')
async def user(user: Annotated[UserCreate,
    Body(..., example={
        'login': 'UserName',
        'password': 'yourPassword'
    })
]):
    ...


@app.get('/user')
async def get_user():
    ...


@app.get('/messages')
async def messages():
    ...

