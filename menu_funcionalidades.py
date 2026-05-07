from menu import menu_clientes, menu_princial, menu_materiaprima, menu_productosfinales, menu_proveedores, menu_reportes, menu_ventas, opcion
from gestion_clientes import input_clientes
from gestion_materiaprima import input_materia_prima
from gestion_proveedores import input_proveedor, input_transaccion_proveedores
from gestion_productosfinales import input_producto_final
from agregar_venta import agregar_venta

def menu_principal():

    while True:

        try:

            menu_princial()
            opc = opcion()

            if opc == 1:
                menu_clientes_funcional()

            elif opc == 2:
                menu_proveedores_funcional()

            elif opc == 3:
                menu_materiaprima_funcional()

            elif opc == 4:
                menu_productosfinales_funcional()

            elif opc == 5:
                menu_ventas_funcional()

            elif opc == 6:
                menu_reportes_funcional()

            elif opc == 7:
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida")

        except:
            print("Ingrese un valor válido")


# ==================== CLIENTES ====================

def menu_clientes_funcional():

    while True:

        try:

            menu_clientes()
            opc = opcion()

            if opc == 1:
                input_clientes()

            elif opc == 2:
                listar_clientes()

            elif opc == 3:
                break

            else:
                print("Opción inválida")

        except:
            print("Ingrese un valor válido")


# ==================== PROVEEDORES ====================

def menu_proveedores_funcional():

    while True:

        try:

            menu_proveedores()
            opc = opcion()

            if opc == 1:
                input_proveedor()

            elif opc == 2:
                input_transaccion_proveedores

            elif opc == 3:
                listar_proveedores()

            elif opc == 4:
                break

            else:
                print("Opción inválida")

        except:
            print("Ingrese un valor válido")


# ==================== MATERIA PRIMA ====================

def menu_materiaprima_funcional():

    while True:

        try:

            menu_materiaprima()
            opc = opcion()

            if opc == 1:
                input_materia_prima()

            elif opc == 2:
                print("Enlistar ordenes")

            elif opc == 3:
                materia_prima()

            elif opc == 4:
                break

            else:
                print("Opción inválida")

        except:
            print("Ingrese un valor válido")


# ==================== PRODUCTOS FINALES ====================

def menu_productosfinales_funcional():

    while True:

        try:

            menu_productosfinales()
            opc = opcion()

            if opc == 1:
                input_producto_final()

            elif opc == 2:
                productos_finales()

            elif opc == 3:
                break

            else:
                print("Opción inválida")

        except:
            print("Ingrese un valor válido")


# ==================== VENTAS ====================

def menu_ventas_funcional():

    while True:

        try:

            menu_ventas()
            opc = opcion()

            if opc == 1:
                agregar_venta()
            elif opc == 2:
                ventas()

            elif opc == 3:
                break

            else:
                print("Opción inválida")

        except:
            print("Ingrese un valor válido")


# ==================== REPORTES ====================
from generar_reportes import productos_finales, listar_clientes, ventas, materia_prima, listar_proveedores


def menu_reportes_funcional():

    while True:

        try:

            menu_reportes()
            opc = opcion()

            if opc == 1:
                listar_clientes()

            elif opc == 2:
                listar_proveedores()

            elif opc == 3:
                materia_prima()

            elif opc == 4:
                productos_finales()

            elif opc == 5:
                ventas()

            elif opc == 6:
                print("Reporte de órdenes de producción...")

            elif opc == 7:
                break

            else:
                print("Opción inválida")

        except:
            print("Ingrese un valor válido")

