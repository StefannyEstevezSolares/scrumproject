
from db import crear, leer_todos, ARCHIVOS
from validaciones_utils import validar_fecha

def input_producto_final():

    nombre = input(
        "Ingrese el nombre del producto: "
    ).strip()

    if nombre == "":
        print("El campo no puede estar vacío")
        return

    descripcion = input(
        "Ingrese una descripción del producto: "
    ).strip()

    if descripcion == "":
        print("El campo no puede estar vacío")
        return

    try:

        precio_venta = float(
            input("Ingrese el precio de venta: ").strip()
        )

    except:
        print("Ingrese un valor válido")
        return

    if precio_venta < 0:
        print("No se permiten números negativos")
        return

    try:

        stock = int(
            input("Ingrese la cantidad en stock: ").strip()
        )

    except:
        print("Ingrese un número válido")
        return

    if stock < 0:
        print("No se permiten números negativos")
        return


    fecha_fabricacion = ""

    while fecha_fabricacion == "":

        fecha_input = input(
            "Ingrese la fecha de fabricación (DD-MM-YYYY): "
        )

        if validar_fecha(fecha_input):
            fecha_fabricacion = fecha_input
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
        "precio_venta": precio_venta,
        "stock": stock,
        "fecha_fabricacion": fecha_fabricacion,
        "fecha_vencimiento (si aplica)": fecha_vencimiento

    }

    crear(ARCHIVOS["productos_finales"], registro)

    print("\nProducto final registrado correctamente")
