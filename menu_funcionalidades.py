from menu import menu_clientes, menu_princial, menu_materiaprima, menu_productosfinales, menu_proveedores, menu_reportes, menu_ventas, opcion
from gestion_clientes import input_clientes
from gestion_materiaprima import input_materia_prima
from gestion_proveedores import input_proveedor, input_transaccion_proveedores
from gestion_productosfinales import input_producto_final
from agregar_venta import agregar_venta
from gestion_ordenes import crear_orden_produccion, limpiar_pantalla
from generar_reportes import productos_finales, listar_clientes, ventas, materia_prima, listar_proveedores, listar_ordenes_produccion


def menu_principal():

    while True:
        limpiar_pantalla()
        try:

            menu_princial()
            opc = opcion()

            if opc == 1:
                menu_clientes_funcional()
                limpiar_pantalla()

            elif opc == 2:
                menu_proveedores_funcional()
                limpiar_pantalla()

            elif opc == 3:
                menu_materiaprima_funcional()
                limpiar_pantalla()

            elif opc == 4:
                menu_productosfinales_funcional()
                limpiar_pantalla()

            elif opc == 5:
                menu_ventas_funcional()
                limpiar_pantalla()

            elif opc == 6:
                menu_reportes_funcional()
                limpiar_pantalla()

            elif opc == 7:
                print("Saliendo del programa...")
                break

            else:
                input("\nOpción inválida.\nPresina Enter para continuar...")

        except:
            input("\nIngrese un valor válido.\nPresiona Enter para continuar...")


# ==================== CLIENTES ====================

def menu_clientes_funcional():

    while True:
        limpiar_pantalla()
        try:

            menu_clientes()
            opc = opcion()

            if opc == 1:
                input_clientes()
                limpiar_pantalla()

            elif opc == 2:
                listar_clientes()
                limpiar_pantalla()

            elif opc == 3:
                break

            else:
                input("\nOpción inválida.\nPresina Enter para continuar...")

        except:
            input("\nIngrese un valor válido.\nPresiona Enter para continuar...")


# ==================== PROVEEDORES ====================

def menu_proveedores_funcional():
    
    while True:
        limpiar_pantalla()
        try:

            menu_proveedores()
            opc = opcion()

            if opc == 1:
                input_proveedor()
                limpiar_pantalla()

            elif opc == 2:
                input_transaccion_proveedores()
                limpiar_pantalla()

            elif opc == 3:
                listar_proveedores()
                limpiar_pantalla()

            elif opc == 4:
                break

            else:
                input("\nOpción inválida.\nPresina Enter para continuar...")

        except:
            input("\nIngrese un valor válido.\nPresiona Enter para continuar...")


# ==================== MATERIA PRIMA ====================

def menu_materiaprima_funcional():

    while True:
        limpiar_pantalla()
        try:

            menu_materiaprima()
            opc = opcion()

            if opc == 1:
                input_materia_prima()
                limpiar_pantalla()

            elif opc == 2:
                crear_orden_produccion()
                limpiar_pantalla()

            elif opc == 3:
                materia_prima()
                limpiar_pantalla()

            elif opc == 4:
                break

            else:
                input("\nOpción inválida.\nPresina Enter para continuar...")

        except:
            input("\nIngrese un valor válido.\nPresiona Enter para continuar...")


# ==================== PRODUCTOS FINALES ====================

def menu_productosfinales_funcional():

    while True:
        limpiar_pantalla()
        try:

            menu_productosfinales()
            opc = opcion()

            if opc == 1:
                input_producto_final()
                limpiar_pantalla()

            elif opc == 2:
                productos_finales()
                limpiar_pantalla()

            elif opc == 3:
                break

            else:
                input("\nOpción inválida.\nPresina Enter para continuar...")

        except:
            input("\nIngrese un valor válido.\nPresiona Enter para continuar...")


# ==================== VENTAS ====================

def menu_ventas_funcional():

    while True:
        limpiar_pantalla()
        try:

            menu_ventas()
            opc = opcion()

            if opc == 1:
                agregar_venta()
                limpiar_pantalla()
            elif opc == 2:
                ventas()
                limpiar_pantalla()

            elif opc == 3:
                break

            else:
                input("\nOpción inválida.\nPresina Enter para continuar...")

        except:
            input("\nIngrese un valor válido.\nPresiona Enter para continuar...")


# ==================== REPORTES ====================

def menu_reportes_funcional():

    while True:
        limpiar_pantalla()
        try:

            menu_reportes()
            opc = opcion()

            if opc == 1:
                listar_clientes()
                limpiar_pantalla()

            elif opc == 2:
                listar_proveedores()
                limpiar_pantalla()

            elif opc == 3:
                materia_prima()
                limpiar_pantalla()

            elif opc == 4:
                productos_finales()
                limpiar_pantalla()

            elif opc == 5:
                ventas()
                limpiar_pantalla()

            elif opc == 6:
                listar_ordenes_produccion()
                limpiar_pantalla()

            elif opc == 7:
                break

            else:
                input("\nOpción inválida.\nPresina Enter para continuar...")

        except:
            input("\nIngrese un valor válido.\nPresiona Enter para continuar...")

