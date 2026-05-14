from pydantic import BaseModel


# =========================
# CLIENTE
# =========================

class Cliente(BaseModel):

    id: int = 0
    nombre: str
    correo: str
    telefono: str


# =========================
# CREAR CLIENTE
# =========================

class ClienteCrear(BaseModel):

    nombre: str
    correo: str
    telefono: str


# =========================
# FACTURA
# =========================

class Factura(BaseModel):

    id: int = 0
    producto: str
    valor: float


# =========================
# TRANSACCION
# =========================

class Transaccion(BaseModel):

    id: int = 0
    tipo: str
    monto: float