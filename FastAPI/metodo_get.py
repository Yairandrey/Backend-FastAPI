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

@app.get("/users")
async def users_class():
    return users_list

# Usando el Path
@app.get("/users/{id}")
async def user(id:int):
    return search_user(id)
    

# Con Query
@app.get("/usersquery/")
async def user(id:int):
    return search_user(id)

# Función para buscar usuario
def search_user(id:int):
    users = filter(lambda user : user.id == id, users_list)
    try:
        return list(users)[0]
    except :
        return "{'error': 'No se encuentra el usuario'}"