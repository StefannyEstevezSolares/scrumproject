from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text
import os
from db import ARCHIVOS, buscar


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
        filas = [[id, p["nombre"], p["descripcion"], f'Q {p["precio_de_venta"]}', p["cantidad_en_stock"], p["fecha_fabricacion"]] for id, p in productos.items()]

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