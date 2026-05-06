import json
import os
import uuid
from pathlib import Path


RUTA_BASE = Path("./data")

RUTA_BASE.mkdir(parents=True, exist_ok=True)

ARCHIVOS = {
    "clientes": RUTA_BASE/'clientes.json',
    "materia_prima": RUTA_BASE/'materia_prima.json',
    "productos_finales": RUTA_BASE/'productos_finales.json',
    "proveedores": RUTA_BASE/'proveedores.json',
    "transacciones_proveedor": RUTA_BASE/'transacciones_proveedor.json',
    "ventas": RUTA_BASE/'ventas.json'
}


def _cargar_datos(archivo):
    """Lee y retorna los datos del archivo JSON. Ahora retorna un diccionario {}."""
    if not os.path.exists(archivo):
        return {}
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def _guardar_datos(archivo, datos):
    """Guarda el diccionario maestro en el archivo JSON."""
    with open(archivo, 'w', encoding='utf-8') as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)


def crear(archivo, registro):
    """Añade un nuevo registro usando un UUID aleatorio como llave principal."""
    datos = _cargar_datos(archivo)
    
    nuevo_id = str(uuid.uuid4()) 
    
    datos[nuevo_id] = registro
    _guardar_datos(archivo, datos)
    
    return nuevo_id, registro


def leer_todos(archivo):
    """Devuelve el diccionario completo con todos los registros."""
    return _cargar_datos(archivo)


def leer_por_id(archivo, id_registro):
    """Busca directamente la llave en el diccionario. Es súper rápido."""
    datos = _cargar_datos(archivo)
    return datos.get(id_registro)


def actualizar(archivo, id_registro, nuevos_datos):
    """Actualiza un registro si su ID existe como llave en el diccionario."""
    datos = _cargar_datos(archivo)
    
    if id_registro in datos:
        datos[id_registro].update(nuevos_datos)
        _guardar_datos(archivo, datos)
        return True
    return False


def eliminar(archivo, id_registro):
    """Elimina directamente la llave del diccionario."""
    datos = _cargar_datos(archivo)
    
    if datos.pop(id_registro, None) is not None:
        _guardar_datos(archivo, datos)
        return True
    return False


def buscar(archivo, parcial=False, **criterios):
    """
    Busca registros según criterios. 
    Si no se envían criterios, devuelve todos los registros.
    """
    datos = _cargar_datos(archivo)
    
    if not criterios:
        return datos

    resultados = {}
    for id_registro, registro in datos.items():
        coincide_alguno = False
        
        for clave, valor_buscado in criterios.items():
            valor_guardado = registro.get(clave)
            
            if valor_guardado is None:
                continue
                
            texto_guardado = str(valor_guardado).lower()
            texto_buscado = str(valor_buscado).lower()
            
            if parcial:
                if texto_buscado in texto_guardado:
                    coincide_alguno = True
                    break
            else:
                if texto_guardado == texto_buscado:
                    coincide_alguno = True
                    break
                    
        if coincide_alguno:
            resultados[id_registro] = registro
            
    return resultados