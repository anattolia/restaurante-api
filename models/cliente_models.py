from pydantic import BaseModel
from datetime import date

class ClienteIn(BaseModel):
    telefono: int


class ClienteOut(BaseModel):
    telefono: int
    nombre: str
    direccion: str
    barrio: str
    cedula: str
    cumpleanos: date

class ClienteInCreate(BaseModel):
    telefono: int
    nombre: str
    direccion: str
    barrio: str
    cedula: str
    cumpleanos: date