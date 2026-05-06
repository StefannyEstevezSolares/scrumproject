from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text


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
