from typing import Dict
from pydantic import BaseModel

class UsuarioInDB(BaseModel):
    username: str
    password: str

database_users = {
    "Admin": UsuarioInDB(**{"username":"Admin",
                            "password":"root"}),

    "Public": UsuarioInDB(**{"username":"Public",
                            "password":"1234"}),
}

def get_usuario(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
        
def update_usuario(user_in_db: UsuarioInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db