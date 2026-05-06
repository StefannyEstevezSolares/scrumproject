import db
import validaciones_utils
import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def validar_cliente():
    clientes = db.leer_todos(db.ARCHIVOS["clientes"])

    if len(clientes) == 0:
       print("Error: No hay clientes registrados")
       return
   
    print("--- CLIENTES ---")

    id_cliente = [id for id in clientes]
    contador = 0


    for id in clientes:
       print(f"{contador}. {clientes[id]['nombre_empresa']}")
       contador += 1

    codigo_cliente = None
   
    while True:
        try:
            opci = int(input("Ingrese el número del cliente que hace la compra: "))
           
            if opci < 0 or opci >= len(clientes):
                print("Error: No existe esa opcion:")
                continue
            else:
                codigo_cliente = id_cliente[opci]
                return codigo_cliente
        except ValueError:
            print("Error: Solo se aceptan números")

def solicitar_producto():
    productos = db.leer_todos(db.ARCHIVOS["productos_finales"])

    if len(productos) == 0:
        print("Error: No hay productos registrados")
        return

    print("--- PRODUCTOS ---")

    id_producto = [id for id in productos]
    contador = 0

    for id in productos:
        print(f"{contador}. {productos[id]['nombre']}")
        contador += 1

    while True:
        try:
            cantidad_productos = int(input("Ingrese la cantidad de productos solicitados: ").strip())


            if cantidad_productos < 0:
                print("Error: La cantidad debe ser mayor a 0")
            else:
                break
        except ValueError:
            print("Error: Solo se permiten números enteros")

    codigos_productos = {}
    total = 0

    for i in range(cantidad_productos):
        calculo = 0
        while True:
            try:
                opci = int(input("-> Ingrese el número del producto: ").strip())
                if opci < 0 or opci >= len(productos):
                    print("Error: No existe esa opcion")
                    continue
                else:
                    producto_seleccionado = id_producto[opci]
                    precio_producto = productos[producto_seleccionado]["precio_venta"]
                    break
            except ValueError:
                print("Error: Solo se aceptan números")

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad deseada: ").strip())

                if cantidad <= 0:
                    print("Error: Solo se permiten numeros mayores a 0")
                    continue
                
                stock = productos[producto_seleccionado]["stock"]

                if stock == 0:
                    print("Error: Ya no hay stock de ese producto")
                    return None,None

                if cantidad > stock:
                    print("Error: La cantidad que desea supera a la cantidad en stock")
                    continue
   
                calculo = precio_producto * cantidad
                codigos_productos[producto_seleccionado] = cantidad
                break
            except ValueError:
                print("Error: Solo se permiten números enteros")
        total += calculo
    return codigos_productos, total


def validar_fecha():


    while True:
        entrada_fecha_creacion = input("Ingrese la fecha de hoy (DD-MM-YY): ")
        fecha_creacion = validaciones_utils.validar_fecha(entrada_fecha_creacion)


        if not fecha_creacion:
            print("Error: Ingrese bien la fecha")
            continue
        else:
            break


    while True:
        entrada_fecha_de_entrega = input("Ingrese la fecha de entrega (DD-MM-YY): ")
        fecha_de_entrega = validaciones_utils.validar_fecha(entrada_fecha_de_entrega)


        if not fecha_de_entrega:
            print("Error: Ingrese bien la fecha")
            continue
        else:
            return entrada_fecha_creacion, entrada_fecha_de_entrega


def estado_venta():
    print("--- ESTADO DE Venta ---")
    estados = ["Pendiente", "En Proceso", "Enviado", "Entregado", "Cancelado"]

    i = 0
    for estado in estados:
        print(f"{i}. {estado}")
        i += 1

    while True:
        try:
            opci = int(input("Ingrese una opción: ").strip())

            if opci == 0:
                return estados[0]
            elif opci == 1:
                return estados[1]
            elif opci == 2:
                return estados[2]
            elif opci == 3:
                return estados[3]
            elif opcio == 4:
                return estados[4]
            else: 
                print("Error: Opción ingresada es inválida")
        except ValueError:
            print("Error: Solo se pueden ingresar números enteros")


def agregar_venta():
    print("--- REGISTRO DE VENTA ---")
    cliente = validar_cliente()
    codigos_productos, total = solicitar_producto()
    if codigos_productos == None and total == None:
        input("\nPresione enter para continuar")
        return
    
    fecha_creacion, fecha_entrega = validar_fecha()
    estado = estado_venta()

    venta = {
        "codigo_cliente": cliente,
        "producto_solicitado": codigos_productos,
        "total": total,
        "fecha_inicio": fecha_creacion,
        "fecha_entrega": fecha_entrega,
        "estado": estado
    }

    for id_producto, valor in codigos_productos.items():
        datos_productos = db.leer_por_id(db.ARCHIVOS["productos_finales"], id_producto)
        stock_actual = datos_productos["stock"]
        stock_nuevo = {
            "stock": stock_actual - valor
        }
        db.actualizar(db.ARCHIVOS["productos_finales"], id_producto, stock_nuevo)

    id_venta, _ = db.crear(db.ARCHIVOS["ventas"], venta)

    limpiar_pantalla()
    print("Confirmacion de datos")
    print(f"Id venta: {id_venta}")
    print(f"Id del Cliente: {cliente}")
    print(f"Productos Solicitados y cantidad: {codigos_productos}")
    print(f"Fecha de inicio: {fecha_creacion}")
    print(f"Fecha de entrega: {fecha_entrega}")
    print(f"Estado de la venta: {estado}")
    input("\nPresione enter para continuar")

def cambiar_estado():
    ventas = db.leer_todos(db.ARCHIVOS["ventas"])

    id_venta = input("Ingrese el id de la venta: ").strip()

    if id_venta in ventas:
        estado = estado_venta()

    nuevo_dato = {
        "estado": estado
    }

    db.actualizar(db.ARCHIVOS["ventas"], id_venta, nuevo_dato)
