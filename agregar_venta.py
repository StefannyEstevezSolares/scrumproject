import db
import validaciones_utils
import os
from generar_reportes import generar_tabla

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
            elif opci == 4:
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


from generar_reportes import generar_tabla
import db

def cambiar_estado():
    termino_busqueda = ""  # Almacena el filtro actual
    while True:
        limpiar_pantalla()
        
        # Carga de datos: Filtrados por búsqueda parcial o todos
        if termino_busqueda == "":
            ventas_dict = db.leer_todos(db.ARCHIVOS["ventas"])
        else:
            ventas_dict = db.buscar(db.ARCHIVOS["ventas"], parcial=True, estado=termino_busqueda)

        # Manejo de casos sin resultados
        if not ventas_dict:
            if termino_busqueda != "":
                print(f"\nNo se encontraron ventas con el estado: '{termino_busqueda}'")
                input("Presione Enter para limpiar la búsqueda...")
                termino_busqueda = ""
                continue
            else:
                print("\nNo hay ventas registradas en el sistema.")
                input("Presione Enter para volver...")
                return

        # Preparación de la tabla
        titulo = f"GESTIÓN DE VENTAS" + (f" (Filtrado por: {termino_busqueda})" if termino_busqueda else "")
        encabezados = ["#", "ID Venta", "Estado", "Total (Q)"]
        alineaciones = ["center", "left", "center", "right"]
        
        filas = []
        mapeo_ids = []
        for i, (id_venta, datos) in enumerate(ventas_dict.items(), start=1):
            filas.append([i, id_venta, datos['estado'], f"Q {datos['total']:,.2f}"])
            mapeo_ids.append(id_venta)

        generar_tabla(titulo, encabezados, filas, alineaciones)

        print("\nOpciones:")
        print("- Ingresa un estado (ej: 'pen') para buscar ventas.")
        print("- Ingresa '#X' (ej: #1) para cambiar el estado de esa fila.")
        print("- Ingresa '-volver' para regresar al menú principal.")
        
        entrada = input("\nSelección / Búsqueda: ").strip().lower()

        if entrada == "-volver":
            break

        # Selección de fila para cambiar estado
        if entrada.startswith("#"):
            try:
                indice = int(entrada[1:]) - 1
                if 0 <= indice < len(mapeo_ids):
                    id_v_seleccionada = mapeo_ids[indice]
                    venta = ventas_dict[id_v_seleccionada]
                    
                    # Restricción: No se permite cambiar si ya está Entregado o Cancelado
                    if venta["estado"] in ["Entregado", "Cancelado"]:
                        print(f"\nError: La venta ya está '{venta['estado']}' y no puede modificarse.")
                        input("Presione Enter para continuar...")
                        continue

                    # Mini menú para seleccionar nuevo estado
                    nuevo_estado = estado_venta() 

                    # Lógica de devolución de stock si se cancela
                    if nuevo_estado == "Cancelado":
                        # Se usa 'codigos_productos' según estructura de ventas.json
                        productos_a_devolver = venta.get("codigos_productos", {})
                        for id_prod, cantidad in productos_a_devolver.items():
                            info_p = db.leer_por_id(db.ARCHIVOS["productos_finales"], id_prod)
                            if info_p:
                                n_stock = info_p["stock"] + cantidad
                                db.actualizar(db.ARCHIVOS["productos_finales"], id_prod, {"stock": n_stock})
                        print("\nStock de productos restaurado.")

                    # Actualización del registro
                    db.actualizar(db.ARCHIVOS["ventas"], id_v_seleccionada, {"estado": nuevo_estado})
                    print(f"\nVenta {id_v_seleccionada} actualizada con éxito.")
                    input("Presione Enter para continuar...")
                else:
                    print("Número de fila fuera de rango.")
                    input("Presione Enter para continuar...")
            except ValueError:
                print("Formato de selección inválido.")
                input("Presione Enter para continuar...")
        
        else:
            # Si no es un comando, se toma como término de búsqueda
            termino_busqueda = entrada