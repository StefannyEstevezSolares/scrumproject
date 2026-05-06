from db import crear, leer_todos, ARCHIVOS
from validaciones_utils import validar_fecha

def input_materia_prima():

    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre == "":
        print("El campo no puede estar vacío")
        return

    descripcion = input("Ingrese una descripción del producto: ").strip()

    if descripcion == "":
        print("El campo no puede estar vacío")
        return


    proveedores = leer_todos(ARCHIVOS["proveedores"])

    print("\nProveedores registrados:")

    for key in proveedores:
        print(key)

    codigo_proveedor = input(
        "Ingrese el código del proveedor: "
    ).strip().lower()


    if codigo_proveedor not in proveedores:
        print("El proveedor no existe en el sistema")
        return

    try:

        stock = int(input("Ingrese la cantidad en stock: ").strip())

    except:
        print("Ingrese un número válido")
        return

    if stock < 0:
        print("No se permiten números negativos")
        return

    try:

        precio_unidad = float(
            input("Ingrese el precio por unidad: ").strip()
        )

    except:
        print("Ingrese un valor válido")
        return

    if precio_unidad < 0:
        print("No se permiten números negativos")
        return


    fecha_adquisicion = ""

    while fecha_adquisicion == "":

        fecha_input = input(
            "Ingrese la fecha de adquisición (DD-MM-YYYY): "
        )

        if validar_fecha(fecha_input):
            fecha_adquisicion = fecha_input
        else:
            print("Fecha no válida")

    fecha_vencimiento = None

    respuesta = input(
        "¿Tiene fecha de vencimiento? (si/no): "
    ).strip().lower()

    if respuesta == "si":

        while fecha_vencimiento == None:

            fecha_input = input(
                "Ingrese la fecha de vencimiento (DD-MM-YYYY): "
            )

            if validar_fecha(fecha_input):
                fecha_vencimiento = fecha_input
            else:
                print("Fecha no válida")

    registro = {

        "nombre": nombre,
        "descripcion": descripcion,
        "codigo_proveedor": codigo_proveedor,
        "stock": stock,
        "precio_unidad": precio_unidad,
        "fecha_adquisicion": fecha_adquisicion,
        "fecha_vencimiento (si aplica)": fecha_vencimiento

    }

    crear("materia_prima.json", registro)

    print("\nMateria prima registrada correctamente")


input_materia_prima()