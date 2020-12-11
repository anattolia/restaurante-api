from pydantic import BaseModel

class ProductoIn(BaseModel):
    id: str
    nombre: str

class ProductoOut(BaseModel):
    id: str
    nombre: str
    precio: int
    cantidad: int
    categoria: str

class ProductoInCreate(BaseModel):
    id: str
    nombre: str
    precio: int
    cantidad: int
    categoria: str