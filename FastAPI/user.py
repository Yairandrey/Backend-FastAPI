from pydantic import BaseModel
from fastapi import FastAPI

# Uso BaseModel para crear un modelo (ENTIDAD) de usuario a trabjar
app = FastAPI()

# Entidad user
class User(BaseModel):
    name : str
    age : int
    id : int

    

users_list = [User(id = 1,name="Yair", age=19),
         User(id = 2, name="Jorge",age=29),
         User(id = 3,name="Carlos",age=39),
         ]



@app.get("/usersjson")
async def get_users():
    return [
        {"name" : "Yair", "age":19},
        {"name" : "Jorge", "age":29},
        {"name" : "Carlos", "age":39},
    ]

@app.get("/userslist")
async def users_class():
    return users_list