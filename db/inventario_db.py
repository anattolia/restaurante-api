from typing import Dict
from pydantic import BaseModel

class ProductoInDB(BaseModel):
    id: str
    nombre: str
    precio: int
    cantidad: int
    categoria: str

database_productos = {
    "CA01": ProductoInDB(**{"id": "CA01",
                                "nombre":"Churrasco",
                                "precio":17000,
                                "cantidad":10,
                                "categoria":"Carnes"
                                }),

    "PE01": ProductoInDB(**{"id": "PE01",
                                "nombre":"Trucha frita",
                                "precio":22000,
                                "cantidad":15,
                                "categoria":"Pescados"
                                }),
}

def create_producto(nuevo_producto: ProductoInDB):
    database_productos[nuevo_producto.id] = nuevo_producto
    return nuevo_producto

def get_producto(id: str):
    if id in database_productos.keys():
        return database_productos[id]
    else:
        return None

def get_all_productos():
    return database_productos.values()
        
def update_producto(producto_in_db: ProductoInDB):
    database_productos[producto_in_db.telefono] = producto_in_db
    return producto_in_db

def delete_producto(producto: ProductoInDB):
    del database_productos[producto.telefono]
    return "El producto ha sido eliminado con éxito"