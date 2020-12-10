from pydantic import BaseModel

class UsuarioIn(BaseModel):
    username: str
    password: str

class UsuarioOut(BaseModel):
    username: str
   



