from fastapi import FastAPI

app = FastAPI()


# Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a mi API con FastAPI"}


# Lista de clientes
clientes = [
    {"id": 1, "nombre": "Juan", "correo": "juan@gmail.com"},
    {"id": 2, "nombre": "Maria", "correo": "maria@gmail.com"},
    {"id": 3, "nombre": "Carlos", "correo": "carlos@gmail.com"}
]


# Mostrar todos los clientes
@app.get("/clientes")
def obtener_clientes():
    return clientes


# Mostrar un solo cliente por ID
@app.get("/clientes/{id}")
def obtener_cliente(id: int):

    for cliente in clientes:
        if cliente["id"] == id:
            return cliente

    return {"error": "Cliente no encontrado"}