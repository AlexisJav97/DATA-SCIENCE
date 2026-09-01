import csv

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


def leer_motores(ruta_archivo: str) -> list[dict[str, str | float | int]]:
    """
    Mediante la ruta del archivo csv se lee la informacion del conjunto de motores que tienes disponible, valida que cada motor tenga sus datos de forma adecuada y mediante esa validacion guarda en una coleccion tipo lista los motores si cumplien

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
    """
    motores = []

    with open(ruta_archivo, "r", encoding = "utf-8") as archivo:
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