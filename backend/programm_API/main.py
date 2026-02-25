from schema import User, UserSingup
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

app = FastAPI()

origins = [
    'http://localhost:3000',
    'http://localhost',
    'http://frontend',
    'http://frontend:80',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post('/user')
async def user(user: Annotated[UserSingup,
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

