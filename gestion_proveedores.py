
from db import crear, leer_todos, ARCHIVOS
from validaciones_utils import validar_fecha, validar_email, validar_telefono_8_digitos


def input_proveedor():

    nombre_empresa = input(
        "Ingrese el nombre de la empresa: "
    ).strip()

    if nombre_empresa == "":
        print("El campo no puede estar vacío")
        return

    direccion = input(
        "Ingrese la dirección: "
    ).strip()

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

    contacto_principal = input(
        "Ingrese el nombre del contacto principal: "
    ).strip()

    if contacto_principal == "":
        print("El campo no puede estar vacío")
        return

    celular = input(
        "Ingrese el celular (8 dígitos): "
    ).strip()

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

    crear("proveedores.json", registro)

    print("\nProveedor registrado correctamente")

input_proveedor()