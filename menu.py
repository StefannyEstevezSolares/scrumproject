
def menu_princial():
    print("""
===========================INDUSTRIAS IAQ =====================
---------------------------------------------------------------
===================BIENVENIDO AL MENÚ PRINCIAL=================
          
            INGRESE UN NÚMERO DEL MENÚ PARA CONTINUAR:
          
          1. Gestión Clientes
          2. Gestión Proveedores
          3. Gestión Materia Prima
          4. Gestión Productos Finales
          5. Gestión Ventas
          6. Gestión Reportes

          PRESIONA "7" PARA SALIR
          
================================================================
================================================================
""")
    

def menu_clientes():
    print("""

===================BIENVENIDO AL MENÚ CLIENTES=================
          
            INGRESE UN NÚMERO DEL MENÚ PARA CONTINUAR:
          
          1. Registrar a un cliente nuevo
          2. Enlistar historial de clientes
          3. Volver

          
================================================================
""")
    
def menu_proveedores():
    print("""

=================BIENVENIDO AL MENÚ PROVEEDORES=================
          
            INGRESE UN NÚMERO DEL MENÚ PARA CONTINUAR:
          
          1. Registrar a un proveedor nuevo
          2. Registrar transaccion de proveedores
          3. Enlistar historial de proveedores
          4. Volver

          
=================================================================
""")
    
def menu_materiaprima():
    print("""

===============BIENVENIDO AL MENÚ MATERIAS PRIMA=================
          
            INGRESE UN NÚMERO DEL MENÚ PARA CONTINUAR:
          
          1. Registrar materia prima
          2. Registrar orden de producción
          3. Enlistar materia prima existente
          4. Cambiar estado de orden de producción
          5. Volver

          
=================================================================
""")
    
def menu_productosfinales():
    print("""

==============BIENVENIDO AL MENÚ DE PRODUCTOS FINALES============
          
            INGRESE UN NÚMERO DEL MENÚ PARA CONTINUAR:
          
          1. Registrar producto final
          2. Enlistar productos finales
          3. Volver

          
=================================================================
""")
    
def menu_ventas():
    print("""

==================BIENVENIDO AL MENU DE VENTAS===================
          
            INGRESE UN NÚMERO DEL MENÚ PARA CONTINUAR:
          
          1. Registrar venta
          2. Enlistar ventas
          3. Cambiar estado de venta
          4. Volver

          
=================================================================
""")
    
def menu_reportes():
    print("""

==================BIENVENIDO AL MENU DE REPORTES===================
          
            INGRESE UN NÚMERO DEL MENÚ PARA CONTINUAR:
          
          1. Reporte de clientes
          2. Reporte de proveedores
          3. Reporte de materia prima
          4. Reporte de productos finales
          5. Reporte de ventas
          6. Reporte de ordenes de producción y su estado
          7. Volver

          
=================================================================
""")
    
def opcion():
    opc= int(input("Ingrese su opción "))
    return opc