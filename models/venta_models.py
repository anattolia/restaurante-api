from pydantic import BaseModel
from datetime import datetime

class VentaIn(BaseModel):
    venta_total: int
    telefono: int
    username: str


class VentaOut(BaseModel):
    venta_id: int 
    venta_fecha: datetime = datetime.now()
    venta_total: int
    telefono: int
    username: str