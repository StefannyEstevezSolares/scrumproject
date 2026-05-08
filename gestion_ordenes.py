from db import ARCHIVOS, crear, leer_todos, actualizar, leer_por_id
from validaciones_utils import validar_fecha
from generar_reportes import limpiar_pantalla


def mostrar_datos(datos):
    """Muestra los datos de la orden de producción."""
    print("\nDatos de la Orden de Producción:")
    print(f"Producto: {datos['producto']}")
    print(f"Códigos de Materias Primas:")
    for codigo in datos["materias_primas"]:
        print(f"  - {datos['materias_primas'][codigo][0]} X{datos['materias_primas'][codigo][1]}")

    print(f"Cantidad a producir: {datos['cantidad_producir']}")
    print(f"Fecha de Inicio: {datos['fecha_inicio']}")
    print(f"Fecha de Finalización: {datos['fecha_finalizacion']}")
    print(f"Estado: {datos['estado']}\n")


def crear_orden_produccion():
    """Crea una nueva orden de producción."""
    datos = {
        "producto": "",
        "producto_codigo" : "",
        "codigos_materias_primas": [],
        "codigos_excluidos_materias_primas": [],
        "materias_primas": {},
        "cantidad": [],
        "cantidad_producir": 0,
        "fecha_inicio": "",
        "fecha_finalizacion": "",
        "estado": "Creando"
    }

    ingresat_materia_prima = True

    materias_primas = leer_todos(ARCHIVOS["materia_prima"])
    materias_primas = {id: values for id, values in materias_primas.items() if values["stock"] > 0}
    if not materias_primas:
        print("No hay materias primas disponibles.\nPor favor, agregue materias primas antes de crear una orden de producción.")
        input("Presione Enter para continuar...")
        return

    while True:
        limpiar_pantalla()
        mostrar_datos(datos)

        if not datos["producto"]:
            productos_finales = leer_todos(ARCHIVOS["productos_finales"])
            if not productos_finales:
                print("No hay productos finales disponibles.\nPor favor, agregue productos finales antes de crear una orden de producción.")
                input("Presione Enter para continuar...")
                return
            
            print("Productos Finales Disponibles:")
            for i, (id, info) in enumerate(productos_finales.items()):
                print(f"{i + 1}. {info['nombre']}")

            input_producto = input("\nIngrese el número del producto final: ").strip()
            if not input_producto.isdigit() or int(input_producto) < 1 or int(input_producto) > len(productos_finales):
                print("Número de producto final inválido. Intente nuevamente.")
                input("Presione Enter para continuar...")
                continue

            producto_seleccionado = list(productos_finales.items())[int(input_producto) - 1]
            datos["producto"] = producto_seleccionado[1]['nombre']
            datos["producto_codigo"] = producto_seleccionado[0]
            continue

        if ingresat_materia_prima:
            for codigo in datos["codigos_excluidos_materias_primas"]:
                materias_primas.pop(codigo, None)
            for codigo in datos["codigos_materias_primas"]:
                materias_primas.pop(codigo, None)
            
            print("\nMaterias Primas Disponibles:")
            for i, (id, info) in enumerate(materias_primas.items()):
                print(f"{i + 1}. {info['nombre']}")

            input_materia = input("\nIngrese el número de la materia prima (o '-fin' para terminar): ").strip().lower()

            if input_materia == "-fin":
                if not datos["codigos_materias_primas"]:
                    print("\nDebe ingresar al menos una materia prima.")
                    input("Presione Enter para continuar...")
                    continue
                else:
                    ingresat_materia_prima = False
                    continue

            if not input_materia.isdigit() or int(input_materia) < 1 or int(input_materia) > len(materias_primas):
                print("Número de materia prima inválido. Intente nuevamente.")
                input("Presione Enter para continuar...")
                continue

            materia_seleccionada = list(materias_primas.items())[int(input_materia) - 1]
            codigo_materia = materia_seleccionada[0]
            nombre_materia = materia_seleccionada[1]['nombre']
            cantidad_materia = materia_seleccionada[1]['stock']

            cantidad_input = input(f"Ingrese la cantidad de '{nombre_materia}' necesaria: ").strip()

            if not cantidad_input.isdigit() or int(cantidad_input) <= 0:
                print("\nCantidad inválida. Debe ser un número entero positivo o mayor a 0.")
                input("Presione Enter para continuar...")
                continue

            cantidad_materia = int(cantidad_input)

            if cantidad_materia > materias_primas[codigo_materia]['stock']:
                print(f"\nNo hay suficiente cantidad de '{nombre_materia}' disponible.\nStock actual: {materias_primas[codigo_materia]['stock']}.")
                if materias_primas[codigo_materia]['stock'] == 0:
                    datos["codigos_excluidos_materias_primas"].append(codigo_materia)
                input("Presione Enter para continuar...")
                continue

            datos["codigos_materias_primas"].append(codigo_materia)
            datos["materias_primas"][codigo_materia] = [nombre_materia, cantidad_materia]
            datos["cantidad"].append(cantidad_materia)
            continue

        if datos["cantidad_producir"] == 0:
            cantidad_producir_input = input("\nIngrese la cantidad a producir: ").strip()

            if not cantidad_producir_input.isdigit() or int(cantidad_input) <= 0:
                print("\nCantidad inválida. Debe ser un número entero positivo o mayor a 0.")
                input("Presione Enter para continuar...")
                continue

            cantidad_producir_input = int(cantidad_producir_input)

            datos["cantidad_producir"] = cantidad_producir_input
            continue

        if not datos["fecha_inicio"]:
            fecha_inicio = input("\nIngrese la fecha de inicio (DD-MM-AAAA): ").strip()
            if not validar_fecha(fecha_inicio):
                print("Fecha de inicio inválida. Intente nuevamente.")
                input("Presione Enter para continuar...")
                continue
            datos["fecha_inicio"] = fecha_inicio
            continue

        if not datos["fecha_finalizacion"]:
            fecha_finalizacion = input("\nIngrese la fecha de finalización (DD-MM-AAAA): ").strip()
            if not validar_fecha(fecha_finalizacion):
                print("Fecha de finalización inválida. Intente nuevamente.")
                input("Presione Enter para continuar...")
                continue
            datos["fecha_finalizacion"] = fecha_finalizacion
            continue
    
        if datos["estado"] == "Creando":
            datos["estado"] = "Pendiente"
            break

    limpiar_pantalla()
    mostrar_datos(datos)
    datos_guardar = {
        "producto": datos["producto_codigo"],
        "codigos_materias_primas": datos["codigos_materias_primas"],
        "cantidad": datos["cantidad"],
        "cantidad_producir": datos["cantidad_producir"],
        "fecha_inicio": datos["fecha_inicio"],
        "fecha_finalizacion": datos["fecha_finalizacion"],
        "estado": datos["estado"]
        }
    
    crear(ARCHIVOS["orden_produccion"], datos_guardar)

    for i in range(len(datos_guardar["codigos_materias_primas"])):
        id_m = datos_guardar["codigos_materias_primas"][i]

        info_m = leer_por_id(ARCHIVOS["materia_prima"], id_m)

        nuevo_stock = info_m["stock"] - datos_guardar["cantidad"][i]
        actualizar(ARCHIVOS["materia_prima"], id_m, {"stock": nuevo_stock})


    print("\nOrden de producción creada exitosamente.")
    input("Presione Enter para continuar...")
