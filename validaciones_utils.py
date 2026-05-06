import re
from datetime import datetime


def validar_fecha(fecha_texto):
    """
    Valida si una fecha tiene el formato DD-MM-YYYY y es una fecha real.
    """
    try:
        datetime.strptime(fecha_texto, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def validar_telefono_8_digitos(telefono):
    """
    Valida que el teléfono contenga exactamente 8 números.
    """
    patron = r"^\d{8}$"
    return bool(re.match(patron, str(telefono)))


def validar_email(email):
    """
    Valida si un correo electrónico tiene una estructura estándar.
    """
    patron = r'^[a-z0-9^\d{8}$_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron, email))
