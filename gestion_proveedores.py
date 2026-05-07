
from db import crear, leer_todos, ARCHIVOS, actualizar
from validaciones_utils import validar_fecha, validar_email, validar_telefono_8_digitos


def input_proveedor():

    nombre_empresa = input("Ingrese el nombre de la empresa: ").strip()

    if nombre_empresa == "":
        print("El campo no puede estar vacío")
        return

    direccion = input("Ingrese la dirección: ").strip()

    if direccion == "":
        print("El campo no puede estar vacío")
        return

    telefono = input(
        "Ingrese el teléfono (8 dígitos): "
    ).strip()

    if telefono == "":
        print("El campo no puede estar vacío")
        return

    if not validar_telefono_8_digitos(telefono):
        print("El teléfono debe contener exactamente 8 números")
        return

    contacto_principal = input("Ingrese el nombre del contacto principal: ").strip()

    if contacto_principal == "":
        print("El campo no puede estar vacío")
        return

    celular = input("Ingrese el celular (8 dígitos): ").strip()

    if celular == "":
        print("El campo no puede estar vacío")
        return

    if not validar_telefono_8_digitos(celular):
        print("El celular debe contener exactamente 8 números")
        return

    email = input(
        "Ingrese el correo electrónico: "
    ).strip().lower()

    if email == "":
        print("El campo no puede estar vacío")
        return

    if not validar_email(email):
        print("Ingrese un correo válido")
        return

    registro = {

        "nombre_empresa": nombre_empresa,
        "direccion": direccion,
        "telefono": telefono,
        "contacto_principal": contacto_principal,
        "celular": celular,
        "email": email

    }

    crear(ARCHIVOS["proveedores"], registro)

    print("\nProveedor registrado correctamente")


def input_transaccion_proveedores():

    proveedores = leer_todos(ARCHIVOS["proveedores"])

    print("\nProveedores registrados:")

    for key in proveedores:
        print(key)

    codigo_proveedor = input("\nIngrese el código del proveedor: ").strip().lower()


    if codigo_proveedor not in proveedores:
        print("El proveedor no existe en el sistema")
        return


    materias_primas = leer_todos(ARCHIVOS["materia_prima"])

    print("\nMaterias primas registradas:")

    for key in materias_primas:
        print(key)

    codigo_materia = input(
        "\nIngrese el código de materia prima: ").strip().lower()


    if codigo_materia not in materias_primas:
        print("La materia prima no existe en el sistema")
        return


    try:
        cantidad = int(
            input("Ingrese la cantidad: ").strip())

    except:
        print("Ingrese un número válido")
        return

    if cantidad < 0:
        print("No se permiten números negativos")
        return

    try:

        precio = float(
            input("Ingrese el precio: ").strip()
        )

    except:
        print("Ingrese un valor válido")
        return

    if precio < 0:
        print("No se permiten números negativos")
        return


    fecha = ""

    while fecha == "":

        fecha_input = input(
            "Ingrese la fecha (DD-MM-YYYY): "
        )

        if validar_fecha(fecha_input):
            fecha = fecha_input
        else:
            print("Fecha no válida")

    registro = {

        "codigo_proveedor": codigo_proveedor,
        "codigo_materia": codigo_materia,
        "cantidad": cantidad,
        "precio": precio,
        "fecha": fecha

    }

    crear(ARCHIVOS["transaccion_proveedores"], registro)

    materia_prima = leer_todos(ARCHIVOS["materia_prima"])

    stock = materia_prima[codigo_materia]["stock"]

    nuevo_stock = {

        "stock" : stock + cantidad
    }

    actualizar(ARCHIVOS["materia_prima"], codigo_materia, nuevo_stock)


    print("\nTransacción registrada correctamente")

input_transaccion_proveedores()