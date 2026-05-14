from fastapi import FastAPI
from modelos.cliente import Cliente, ClienteCrear, Factura, Transaccion

app = FastAPI()


# =========================
# LISTAS
# =========================

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []


# =========================
# FUNCION AUTOINCREMENTO
# =========================

def generar_id(lista):

    if lista:
        return max(obj.id for obj in lista) + 1

    return 1


# =========================
# RUTA PRINCIPAL
# =========================

@app.get("/")
def inicio():

    return {
        "mensaje": "Bienvenido a la API"
    }


# =========================
# CLIENTES
# =========================

# Listar clientes
@app.get("/clientes")
def listar_clientes():

    return {
        "clientes": lista_clientes
    }


# Obtener cliente por ID
@app.get("/clientes/{id}")
def obtener_cliente(id: int):

    for cliente in lista_clientes:

        if cliente.id == id:
            return cliente

    return {
        "error": "Cliente no encontrado"
    }


# Crear cliente
@app.post("/clientes", response_model=Cliente)
def crear_cliente(datos_cliente: ClienteCrear):

    cliente_val = Cliente.model_validate(
        datos_cliente.model_dump()
    )

    cliente_val.id = generar_id(lista_clientes)

    lista_clientes.append(cliente_val)

    return cliente_val


# Editar cliente
@app.put("/clientes/{id}", response_model=Cliente)
def editar_cliente(id: int, datos_cliente: ClienteCrear):

    for i, obj_cliente in enumerate(lista_clientes):

        if obj_cliente.id == id:

            cliente_val = Cliente.model_validate(
                datos_cliente.model_dump()
            )

            cliente_val.id = id

            lista_clientes[i] = cliente_val

            return cliente_val

    return {
        "error": "Cliente no encontrado"
    }


# Eliminar cliente
@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    for cliente in lista_clientes:

        if cliente.id == id:

            lista_clientes.remove(cliente)

            return {
                "mensaje": f"Cliente con ID {id} eliminado correctamente",
                "cliente": cliente
            }

    return {
        "error": "Cliente no encontrado"
    }


# =========================
# FACTURAS
# =========================

# Listar facturas
@app.get("/facturas")
def listar_facturas():

    return {
        "facturas": lista_facturas
    }


# Crear factura
@app.post("/facturas")
def crear_factura(factura: Factura):

    factura.id = generar_id(lista_facturas)

    lista_facturas.append(factura)

    return {
        "mensaje": "Factura creada correctamente",
        "factura": factura
    }


# Eliminar factura
@app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for factura in lista_facturas:

        if factura.id == id:

            lista_facturas.remove(factura)

            return {
                "mensaje": f"Factura con ID {id} eliminada correctamente",
                "factura": factura
            }

    return {
        "error": "Factura no encontrada"
    }


# =========================
# TRANSACCIONES
# =========================

# Listar transacciones
@app.get("/transacciones")
def listar_transacciones():

    return {
        "transacciones": lista_transacciones
    }


# Crear transacción
@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):

    transaccion.id = generar_id(lista_transacciones)

    lista_transacciones.append(transaccion)

    return {
        "mensaje": "Transacción creada correctamente",
        "transaccion": transaccion
    }


# Eliminar transacción
@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):

    for transaccion in lista_transacciones:

        if transaccion.id == id:

            lista_transacciones.remove(transaccion)

            return {
                "mensaje": f"Transacción con ID {id} eliminada correctamente",
                "transaccion": transaccion
            }

    return {
        "error": "Transacción no encontrada"
    }