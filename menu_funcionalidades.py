from menu import menu_clientes, menu_princial, menu_materiaprima, menu_productosfinales, menu_proveedores, menu_reportes, menu_ventas, opcion
from gestion_clientes import input_clientes
from gestion_materiaprima import input_materia_prima
from gestion_proveedores import input_proveedor, input_transaccion_proveedores
from gestion_productosfinales import input_producto_final
from agregar_venta import agregar_venta, cambiar_estado
from gestion_ordenes import crear_orden_produccion, limpiar_pantalla
from generar_reportes import productos_finales, listar_clientes, ventas, materia_prima, listar_proveedores, listar_ordenes_produccion


def menu_principal():

    while True:
        limpiar_pantalla()
        try:

            menu_princial()
            opc = opcion()

            if opc == 1:
                limpiar_pantalla()
                menu_clientes_funcional()

            elif opc == 2:
                limpiar_pantalla()
                menu_proveedores_funcional()

            elif opc == 3:
                limpiar_pantalla()
                menu_materiaprima_funcional()

            elif opc == 4:
                limpiar_pantalla()
                menu_productosfinales_funcional()

            elif opc == 5:
                limpiar_pantalla()
                menu_ventas_funcional()

            elif opc == 6:
                limpiar_pantalla()
                menu_reportes_funcional()

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
                limpiar_pantalla()
                input_clientes()

            elif opc == 2:
                limpiar_pantalla()
                listar_clientes()

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
                limpiar_pantalla()
                input_proveedor()

            elif opc == 2:
                limpiar_pantalla()
                input_transaccion_proveedores()

            elif opc == 3:
                limpiar_pantalla()
                listar_proveedores()

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
                limpiar_pantalla()
                input_materia_prima()

            elif opc == 2:
                limpiar_pantalla()
                crear_orden_produccion()

            elif opc == 3:
                limpiar_pantalla()
                materia_prima()

            elif opc == 4:
                limpiar_pantalla()
                listar_ordenes_produccion()

            elif opc == 5:
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
                limpiar_pantalla()
                input_producto_final()

            elif opc == 2:
                limpiar_pantalla()
                productos_finales()

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
                limpiar_pantalla()
                agregar_venta()

            elif opc == 2:
                limpiar_pantalla()
                ventas()

            elif opc == 3:
                limpiar_pantalla()
                cambiar_estado()

            elif opc == 4:
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
                limpiar_pantalla()
                listar_clientes()

            elif opc == 2:
                limpiar_pantalla()
                listar_proveedores()

            elif opc == 3:
                limpiar_pantalla()
                materia_prima()

            elif opc == 4:
                limpiar_pantalla()
                productos_finales()

            elif opc == 5:
                limpiar_pantalla()
                ventas()

            elif opc == 6:
                limpiar_pantalla()
                listar_ordenes_produccion()

            elif opc == 7:
                break

            else:
                input("\nOpción inválida.\nPresina Enter para continuar...")

        except:
            input("\nIngrese un valor válido.\nPresiona Enter para continuar...")

