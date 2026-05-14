from fastapi import FastAPI

app = FastAPI()

# Base de datos simulada
clientes = [
    {
        "id": 1,
        "nombre": "Juan",
        "correo": "juan@gmail.com",
        "telefono": "3001234567"
    },
    {
        "id": 2,
        "nombre": "Maria",
        "correo": "maria@gmail.com",
        "telefono": "3019876543"
    },
    {
        "id": 3,
        "nombre": "Carlos",
        "correo": "carlos@gmail.com",
        "telefono": "3024567890"
    }
]


# Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "API de Clientes"}


# Mostrar todos los clientes
@app.get("/clientes")
def obtener_clientes():
    return clientes


# Mostrar un cliente por ID
@app.get("/clientes/{id}")
def obtener_cliente(id: int):

    for cliente in clientes:
        if cliente["id"] == id:
            return cliente

    return {"error": "Cliente no encontrado"}