from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text
import os
from db import ARCHIVOS, buscar, leer_por_id


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def generar_tabla(titulo, encabezados, datos, alineaciones=None):
    """
    Genera una tabla
    """
    console = Console()
    
    if alineaciones is None or len(alineaciones) != len(encabezados):
        alineaciones = ["center"] * len(encabezados)
    
    tabla = Table(
        title=f"\n{titulo}",
        title_style="bold blue",
        box=box.DOUBLE_EDGE, 
        header_style="bold green", 
        expand=True,
    )

    for col_nombre, alinea_datos in zip(encabezados, alineaciones):
        tabla.add_column(
            Text(col_nombre, justify="center"), 
            justify=alinea_datos, 
            ratio=1,
            no_wrap=False,
            overflow="ellipsis"
        )

    for fila in datos:
        tabla.add_row(*map(str, fila))

    console.print(tabla)


def productos_finales():
    """Genera un reporte de productos finales y busqueda."""
    productos = {}
    while True:
        limpiar_pantalla()
        if not productos:
            productos = buscar(ARCHIVOS["productos_finales"], parcial=True, nombre="", fecha_fabricacion="")
            if not productos:
                limpiar_pantalla()
                print("\nNo hay productos finales registrados.")
                input("Presiona Enter para continuar...\n")
                return

        titulo = "Reporte de Productos Finales"
        encabezados = ["ID", "Nombre", "Descripción", "Precio de Venta (Q)", "Cantidad en Stock", "Fecha de Fabricación"]
        alineaciones = ["center", "left", "left", "right", "center", "center"]
        filas = [[id, p["nombre"], p["descripcion"], f'Q {p["precio_venta"]}', p["stock"], p["fecha_fabricacion"]] for id, p in productos.items()]

        generar_tabla(titulo, encabezados, filas, alineaciones)

        print ("\nPuedes buscar un producto por Nombre o Fecha de Fabricación.")
        buscar_input = input("Ingresa el término de búsqueda (o ingresa -Volver para regresar): ").strip().lower()

        if buscar_input == "":
            limpiar_pantalla()
            print("\nLa búsqueda no puede estar vacía.")
            input("Presiona Enter para continuar...\n")
            productos = {}
            continue
        if buscar_input == "-volver":
            return
        
        productos = buscar(ARCHIVOS["productos_finales"], parcial=True, nombre=buscar_input, fecha_fabricacion=buscar_input)

        if not productos:
            limpiar_pantalla()
            print("\nNo se encontraron productos que coincidan con la búsqueda.")
            input("Presiona Enter para continuar...\n")
            productos = {}


def listar_clientes():
    """Genera un reporte de clientes y busqueda."""
    clientes = {}
    while True:
        limpiar_pantalla()
        if not clientes:
            clientes = buscar(ARCHIVOS["clientes"], parcial=True, nombre_de_la_empresa="", contacto_principal="")
            if not clientes:
                limpiar_pantalla()
                print("\nNo hay clientes registrados.")
                input("Presiona Enter para continuar...\n")
                return

        titulo = "Reporte de Clientes"
        encabezados = ["#", "ID", "Nombre de la Empresa", "Dirección", "Teléfono", "Contacto Principal", "Celular", "Correo Electrónico"]
        alineaciones = ["center", "left", "left", "center", "left", "center", "left"]
        filas = [[i, id, c["nombre_empresa"], c["direccion"], c["telefono"], c["contacto_principal"], c["celular"], c["email"]] for i, (id, c) in enumerate(clientes.items(), start=1)]

        generar_tabla(titulo, encabezados, filas, alineaciones)

        print ("\nPuedes buscar un cliente por Nombre de la Empresa, Contacto Principal o Correo.")
        print("Para ver el historial de compras de un cliente, ingresa el número correspondiente a su fila. ej: #3")
        buscar_input = input("Ingresa el término de búsqueda (o ingresa -Volver para regresar): ").strip().lower()

        if buscar_input == "":
            limpiar_pantalla()
            print("\nLa búsqueda no puede estar vacía.")
            input("Presiona Enter para continuar...\n")
            clientes = {}
            continue

        if buscar_input == "-volver":
            return
        
        if buscar_input.startswith("#"):
            try:
                index = int(buscar_input[1:]) - 1
                if 0 <= index < len(filas):
                    cliente_id = filas[index][1]
                    nombre = filas[index][2]
                    historial_compras(cliente_id, nombre)
                else:
                    raise ValueError
            except ValueError:
                limpiar_pantalla()
                print("\nNúmero de fila inválido.")
                input("Presiona Enter para continuar...\n")
            continue
        
        clientes = buscar(ARCHIVOS["clientes"], parcial=True, nombre_de_la_empresa=buscar_input, contacto_principal=buscar_input, correo_electronico=buscar_input)

        if not clientes:
            limpiar_pantalla()
            print("\nNo se encontraron clientes que coincidan con la búsqueda.")
            input("Presiona Enter para continuar...\n")
            clientes = {}


def historial_compras(cliente_id, nombre_cliente):
    """Genera un reporte del historial de compras de un cliente."""
    limpiar_pantalla()
    compras_usuario = buscar(ARCHIVOS["ventas"], codigo_cliente=cliente_id)

    titulo = f'Historial de Compras del Cliente: {nombre_cliente}'
    encabezados = ["ID", "Productos Comprados", "Total (Q)", "Fecha de Inicio", "Fecha de Entrega", "Estado"]
    alineaciones = ["left", "left", "right", "center", "center", "center"]
    filas = []

    for id, compra in compras_usuario.items():
        productos_comprados = []
        for prod_id, cantidad in compra["codigos_productos"].items():
            producto = leer_por_id(ARCHIVOS["productos_finales"], prod_id)
            if producto:
                productos_comprados.append(f"{producto['nombre']} (x{cantidad})")
        
        filas.append([id, "\n".join(productos_comprados), f'Q {compra["total"]:,}', compra["fecha_inicio"], compra["fecha_entrega"], compra["estado"]])

    generar_tabla(titulo, encabezados, filas, alineaciones)

    input("\nPresiona Enter para regresar a la lista de clientes...\n")


def ventas():
    """Genera un reporte de ventas y busqueda."""
    ventas = {}
    while True:
        limpiar_pantalla()
        if not ventas:
            ventas = buscar(ARCHIVOS["ventas"], parcial=True, codigo_cliente="", fecha_inicio="", fecha_entrega="", estado="")
            if not ventas:
                limpiar_pantalla()
                print("\nNo hay ventas registradas.")
                input("Presiona Enter para continuar...\n")
                return

        titulo = "Reporte de Ventas"
        encabezados = ["ID", "Código Cliente", "Nombre Cliente", "Productos", "Total (Q)", "Fecha de Inicio", "Fecha de Entrega", "Estado"]
        alineaciones = ["left", "left", "left", "left", "right", "center", "center", "center"]
        filas = []

        for id, venta in ventas.items():
            cliente = leer_por_id(ARCHIVOS["clientes"], venta["codigo_cliente"])
            nombre_cliente = cliente["nombre_empresa"] if cliente else "Desconocido"
            productos_comprados = []
            for prod_id, cantidad in venta["codigos_productos"].items():
                producto = leer_por_id(ARCHIVOS["productos_finales"], prod_id)
                if producto:
                    productos_comprados.append(f"{producto['nombre']} (x{cantidad})")
            
            filas.append([id, venta["codigo_cliente"], nombre_cliente, "\n".join(productos_comprados), f'Q {venta["total"]:,}', venta["fecha_inicio"], venta["fecha_entrega"], venta["estado"]])

        generar_tabla(titulo, encabezados, filas, alineaciones)

        print ("\nPuedes buscar una venta por Nombre de Cliente, Fechas o Estado.")
        buscar_input = input("Ingresa el término de búsqueda (o ingresa -Volver para regresar): ").strip().lower()

        if buscar_input == "":
            limpiar_pantalla()
            print("\nLa búsqueda no puede estar vacía.")
            input("Presiona Enter para continuar...\n")
            ventas = {}
            continue
        if buscar_input == "-volver":
            return

        clientes_encontrados = buscar(ARCHIVOS["clientes"], parcial=True, nombre_empresa=buscar_input)

        ventas = buscar(ARCHIVOS["ventas"], parcial=True, fecha_inicio=buscar_input, fecha_entrega=buscar_input, estado=buscar_input)
        for cliente_id in clientes_encontrados.keys():
            ventas_cliente = buscar(ARCHIVOS["ventas"], parcial=True, codigo_cliente=cliente_id)
            ventas.update(ventas_cliente)

        if not ventas:
            limpiar_pantalla()
            print("\nNo se encontraron ventas que coincidan con la búsqueda.")
            input("Presiona Enter para continuar...\n")
            ventas = {}
