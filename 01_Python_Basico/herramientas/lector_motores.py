"""
Módulo encargado de leer y validar datos de motores desde archivos CSV.

Responsabilidad:
    - Leer motores desde un archivo CSV.
    - Convertir los datos a tipos numéricos.
    - Descartar motores con datos inválidos.

Funciones principales:
    - validar_datos()
    - leer_motores()

Dependencias:
    - csv

Usado por:
    - main.py
"""

import csv
from pathlib import Path

def validar_datos(diccionario) -> tuple[str, float | None, float | None, int | None, bool]:
    """
    Convierte y valida los datos de un motor.

    Si voltaje, corriente o RPM no pueden convertirse
    al tipo numérico correspondiente, el valor se mantiene
    como None y la validación general se marca como False.

    Parámetros:
        diccionario:
            Diccionario con los datos de un motor.

    Retorna:
        Tupla en el siguiente orden:

        1. id del motor
        2. voltaje [V]
        3. corriente [A]
        4. rpm
        5. validación:
            True  -> todos los datos son válidos
            False -> al menos un dato es inválido
    """
    dato_valido = True

    voltaje = None
    corriente = None
    rpm = None

    try:
        voltaje = float(diccionario['voltaje'])
    except ValueError:
        print(f"Voltaje invalido en {diccionario['id']}")
        dato_valido = False
    try:
        corriente = float(diccionario['corriente'])
    except ValueError:
        print(f"corriente invalido en {diccionario['id']}")
        dato_valido = False
    try:
        rpm = int(diccionario['rpm'])
    except ValueError:
        print(f"rpm invalido en {diccionario['id']}")
        dato_valido = False


    return diccionario['id'], voltaje, corriente, rpm, dato_valido


def leer_motores(ruta_archivo: str | Path) -> list[dict[str, str | float | int]]:
    """
    Lee y valida los motores almacenados en un archivo CSV.

    Paràmetros:
        ruta_archivo:
            Ruta del archivo CSV.
    
    Retorna:
        Lista de diccionarios con la estructura:

        {
            "id": str,
            "voltaje": float,
            "corriente": float,
            "rpm": int
        }

    Excepciones:
        TypeError:
            Si la ruta no es una cadena ni un objeto Path.

        ValueError:
            Si se recibe una cadena vacía como ruta.

        FileNotFoundError:
            Si el archivo indicado no existe.

        IsADirectoryError:
            Si la ruta corresponde a una carpeta y no a un archivo.

        OSError:
            Si el sistema no puede abrir o leer el archivo.
    """
    if not isinstance(ruta_archivo, (str, Path)):
        raise TypeError(
            "La ruta debe ser una cadena o un objeto Path."
        )

    if isinstance(ruta_archivo, str) and not ruta_archivo.strip():
        raise ValueError(
            "No se ingresó la ruta del archivo de motores."
        )

    ruta = Path(ruta_archivo)
    if not ruta.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {ruta}"
        )

    if not ruta.is_file():
        raise IsADirectoryError(
            f"La ruta no corresponde a un archivo: {ruta}"
        )

    motores = []

    with ruta.open("r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for motor in lector:
            motor_id, voltaje, corriente, rpm,  validacion = validar_datos(motor)

            if validacion:
                motor_valido = {"id": motor_id, "voltaje": voltaje,  "corriente": corriente, "rpm": rpm}
                motores.append(motor_valido)
    return motores

if __name__ == "__main__":
    ruta = r"C:\Users\AlexisJav\Desktop\DATA SCIENCE\01_Python_Basico\motores.csv"
    print(leer_motores(ruta))
