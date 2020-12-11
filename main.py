from db.usuario_db import UsuarioInDB
from db.usuario_db import update_usuario, get_usuario
from models.usuario_models import UsuarioIn, UsuarioOut
from db.cliente_db import ClienteInDB
from db.cliente_db import update_cliente, get_cliente, create_cliente, eliminate_cliente, get_all_clientes
from models.cliente_models import ClienteIn, ClienteOut, ClienteInCreate
from db.inventario_db import ProductoInDB
from db.inventario_db import update_producto, get_producto, create_producto, delete_producto, get_all_productos
from models.inventario_models import ProductoIn, ProductoOut, ProductoInCreate
from models.venta_models import VentaIn, VentaOut
from db.venta_db import VentaInDB, get_all_ventas,save_venta,get_venta

import datetime

from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

@api.post("/usuario/autenticacion/")
async def auth_user(user_in: UsuarioIn):
    user_in_db =get_usuario(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=401, detail="Error en la autenticación")
    return {"Autenticado": True}

@api.post("/usuario/crear/") 
async def create_user(user_in: UsuarioIn):
    user_in_db=update_usuario(user_in)
    user_out = UsuarioOut(**user_in_db.dict())
    user_new = get_usuario(user_out.username)
    if user_new == None:
        raise HTTPException(status_code=404,detail="El usuario no ha sido creado")
    return {"Creado": True}

@api.get("/cliente/consulta/{telefono}")
async def buscar_cliente(telefono: int):
    cliente_in_db = get_cliente(telefono)
    if cliente_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El cliente no existe")
    cliente_out = ClienteOut(**cliente_in_db.dict())
    return cliente_out   

@api.get("/cliente/lista/")
async def buscar_clientes():
    clientes_in_db = get_all_clientes()
    clientes_out = []
    for cliente in clientes_in_db:
        cliente_out = ClienteOut(**cliente.dict())
        clientes_out.append(cliente_out)
    return clientes_out

@api.post("/cliente/crear/") 
async def crear_cliente(cliente_in: ClienteInCreate):
    cliente_in_db = create_cliente(cliente_in)
    cliente_out = ClienteOut(**cliente_in_db.dict())
    return cliente_out

@api.put("/cliente/update/")
async def upd_cliente(cliente_in: ClienteInCreate):
    cliente_in_db = get_cliente(cliente_in.telefono)
    if cliente_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El cliente no existe")
    
    cliente_in_db = ClienteInCreate(**cliente_in.dict())

    update_cliente(cliente_in_db)
    
    update_out = ClienteOut(**cliente_in_db.dict())
    return update_out

@api.delete("/cliente/delete/") 

async def delete_cliente(cliente_in: ClienteIn):
    cliente_in_db = get_cliente(cliente_in.telefono)
    if cliente_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El cliente no existe")
    cliente_out = eliminate_cliente(cliente_in_db)
    return cliente_out

#####Inventario

@api.post("/producto/crear/") 
async def crear_producto(producto_in: ProductoInCreate):
    producto_in_db = create_producto(producto_in)
    producto_out = ProductoOut(**producto_in_db.dict())
    return producto_out

@api.get("/producto/consulta/{id}")
async def buscar_producto(id: str):
    producto_in_db = get_producto(id)
    if producto_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El producto no existe")
    producto_out = ProductoOut(**producto_in_db.dict())
    return producto_out  

@api.get("/producto/lista/")
async def buscar_productos():
    productos_in_db = get_all_productos()
    productos_out = []
    for producto in productos_in_db:
        producto_out = ProductoOut(**producto.dict())
        productos_out.append(producto_out)
    return productos_out

@api.put("/producto/update/")
async def update_producto(producto_in: ProductoInCreate):
    producto_in_db = get_producto(producto_in.id)
    if producto_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El producto no existe")
    
    producto_in_db = ProductoInCreate(**producto_in.dict())

    update_producto(producto_in_db)
    
    update_out = ProductoOut(**producto_in_db.dict())
    return update_out

@api.delete("/producto/delete/") 

async def delete_producto(producto_in: ProductoIn):
    producto_in_db = get_producto(producto_in.id)
    if producto_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El producto no existe")
    producto_out = delete_producto(producto_in_db)
    return producto_out

@api.get("/venta/list/")
async def lista_ventas():
    ventas_in_db = get_all_ventas()
    ventas_out = []
    for venta in ventas_in_db:
        venta_out = VentaOut(**venta.dict())
        ventas_out.append(venta_out)
    return ventas_out


@api.put("/venta/make/")
async def make_venta(venta_in: VentaIn):
    
    user_in_db = get_usuario(venta_in.username)

    if user_in_db == None:
        
        raise HTTPException(status_code=404, detail="El usuario no tiene permisos para hacer ventas"
     ### venta_total = acá tendría en cuenta la cantidad de productos y precio del producto para saber el precio total de acuerdo a inventario
    venta_in_db = VentaInDB(**venta_in.dict())
    venta_in_db = save_venta(venta_in_db)
    venta_out = VentaOut(**venta_in_db.dict())

    return  venta_out    

@api.get("/venta/consulta/{telefono}")
async def buscar_venta(telefono: int):
    venta_in_db = get_all_ventas(telefono)
    if venta_in_db == None:
        raise HTTPException(status_code=404,