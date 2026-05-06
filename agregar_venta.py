import db

def listar_clientes():
    clientes = db.leer_todos(db.ARCHIVOS["clientes"])

    if len(clientes) == 0:
       print("NO hay clientes")
       return

    contador = 0
    
    id_clientes = [id for id in clientes]
    
    for id in clientes:
       
       print(f"{contador}. {clientes[id]['nombre_de_la_empresa']}") 
       contador += 1

    codigo_cliente = None
    
    while True:
        try:
            opci = int(input("Ingrese el número del cliente: "))
            
            if opci < 0 or opci > len(clientes):
                print("Error: No existe esa opcion:")
                continue
            else:
                codigo_cliente = id_clientes[opci]
                print(codigo_cliente)
                return codigo_cliente
        except Exception:
            print("Error: Solo se aceptan números")
            

def agregar_venta():

    id = db.crear(db.ARCHIVOS["ventas"])
    id_cliente = listar_clientes()
    print(id_cliente)

