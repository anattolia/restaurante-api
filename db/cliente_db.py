from datetime import date
from typing import Dict
from pydantic import BaseModel

class ClienteInDB(BaseModel):
    telefono: int
    nombre: str
    direccion: str
    barrio: str
    cedula: str
    cumpleanos: date


database_clientes = {
    3214567895: ClienteInDB(**{"telefono": 3214567895,
                                "nombre":"Pepe",
                                "direccion":"Calle 12 # 20 - 22",
                                "barrio":"Colombia",
                                "cedula":"456123789",
                                "cumpleanos": '1980-2-20'
                                }),

    3007894561: ClienteInDB(**{"telefono": 3007894561,
                                "nombre":"Pepita",
                                "direccion":"Carrera 20 # 15 - 12",
                                "barrio":"Parnaso",
                                "cedula":"1123456789",
                                "cumpleanos": '1985-1-10'
                                }),
}

def get_cliente(telefono: int):
    if telefono in database_clientes.keys():
        return database_clientes[telefono]
    else:
        return None
        
def update_cliente(cliente_in_db: ClienteInDB):
    database_clientes[cliente_in_db.telefono] = cliente_in_db
    return cliente_in_db

def create_cliente(nuevo_cliente: ClienteInDB):
    database_clientes[nuevo_cliente.telefono] = nuevo_cliente
    return nuevo_cliente

def eliminate_cliente(cliente: ClienteInDB):
    del database_clientes[cliente.telefono]
    return "Se elimino satisfactoriamente"

def get_all_clientes():
    return database_clientes.values()