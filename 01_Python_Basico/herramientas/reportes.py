"""
Módulo encargado de generar reportes de motores.

Responsabilidad:
    - Mostrar todos los motores disponibles
    - Mostrar el análisis de los motores
    - Guardar reportes de motores en archivos CSV.

Funciones principales:
    - mostrar_motores()
    - mostrar_analisis_motores()
    - mostrar_estadisticas_motores()
    - guardar_reporte_csv()

Dependencias:
    -lector_motores.py
    -analizar_motor.py
Usado por:
    - main.py
"""


from .lector_motores import leer_motores
from .analisis_motor import analizar_motor, estadistica_motores
import csv

def mostrar_motores(motores: list[dict]) -> None:
    """
    Muestra los motores disponibles.

    Parámetros:
        motores:
            Lista de diccionarios con información
            validada de motores.

    Ejemplo de estructura:
        {
            "id": "M1",
            "voltaje": 24,
            "corriente": 3.2,
            "rpm": 1500
        }

    Retorna:
        None
    """

    print("=== MOTORES DISPONIBLES ===")
    print()
    for motor in motores:
        print(f"Motor: {motor['id']}")
        print(f"voltaje: {motor['voltaje']} V")
        print(f"Corriente: {motor['corriente']} A")
        print(f"RPM: {motor['rpm']}")
        print(5*"-------")

def mostrar_analisis_motores(motores: list[dict]) -> None:
    """
    Muestra parametros de consumo y fisicos de cada motor.

    Parámetros:
        motores:
            Lista de diccionarios con información
            validada de motores.

    Ejemplo de estructura:

            {
                "id": "M1",
                "voltaje": 24,
                "corriente": 3.2,
                "rpm": 1500
            }

    Retorna:
                None
    """
    print("========== ANÁLISIS DE MOTORES ==========")
    print()
    for motor in motores:
        print(f"Motor: {motor['id']}")
        print(f"Voltaje: {motor['voltaje']} V")
        print(f"Corriente: {motor['corriente']} A")
        print(f"RPM: {motor['rpm']}")
        potencia, resistencia, rad_s = analizar_motor(voltaje= motor['voltaje'],
                       corriente= motor['corriente'],
                       rpm= motor['rpm'])
        print(f"Potencia: {potencia:.2f} W")
        print(f"Resistencia: {resistencia:.2f} ohm")
        print(f"Velocidad angular: {rad_s:.2f} rad/s")
        print(5*"-------")

def mostrar_estadisticas_motores(motores: list[dict]) -> None:

    """
    Calcula y muestra las estadísticas generales de los motores.

    Parámetros:
        motores:
            Lista de diccionarios con la información
            validada de los motores.

    Retorna:
        None
    """
    try:
        estadisticos = estadistica_motores(motores)
        print("========== ESTADÍSTICAS DE MOTORES ==========")
        print()
        print(f"Cantidad de motores: {estadisticos['total_motores']}")
        print(f"Voltaje promedio: {estadisticos['voltaje_promedio']:.2f} V")
        print(f"Corriente promedio: {estadisticos['corriente_promedio']:.2f} A")
        print(f"RPM promedio: {estadisticos['rpm_promedio']:.2f} RPM")
        print(f"Potencia promedio: {estadisticos['potencia_promedio']:.2f} W")
        print()
        print("Mayor potencia:")
        print(f"Motor: {estadisticos['motor_mayor_potencia']}")
        print(f"Potencia: {estadisticos['potencia_maxima']:.2f} W")
        print()
        print("Menor potencia:")
        print(f"Motor: {estadisticos['motor_menor_potencia']}")
        print(f"Potencia: {estadisticos['potencia_minima']:.2f} W")

    except ValueError as error:
        print(f"Error: {error}")

def guardar_reporte_csv(motores: list[dict], ruta_salida: str) -> None:
    """
    Genera y guarda un reporte CSV con el análisis de los motores.

    Para cada motor calcula la potencia, la resistencia y la
    velocidad angular. El archivo contiene una fila por motor.

    Parámetros:
        motores:
            Lista de diccionarios con la información validada
            de los motores.

            Ejemplo de estructura:

                {
                    "id": "M1",
                    "voltaje": 24.0,
                    "corriente": 3.2,
                    "rpm": 1500
                }

        ruta_salida:
            Ruta en la que se creará el archivo CSV.

            Si ya existe un archivo en esa ruta, será
            sobrescrito.

    Retorna:
        None

    Excepciones:
        ValueError:
            Si la lista de motores está vacía o no se proporciona
            una ruta de salida válida.

        OSError:
            Si ocurre un problema al crear o escribir el archivo.
    """

    if not mostrar_motores:
        raise ValueError("No existen motores para generar el reporte.")
    
    if not ruta_salida.strip():
        raise ValueError("No se ingresó la ruta de salida del reporte.")

    campos = ["id","voltaje_v","corriente_a","rpm","potencia_w","resistencia_ohm","velocidad_angular_rad_s"]
    reporte_motores = []

    for motor in motores:
        potencia, resistencia, rad_s = analizar_motor(voltaje= motor['voltaje'],
            corriente= motor['corriente'],
            rpm= motor['rpm'])

        reporte_motores.append({"id":motor['id'],
                                "voltaje_v": motor['voltaje'],
                                "corriente_a": motor['corriente'],
                                "rpm": motor['rpm'],
                                "potencia_w": round(potencia,2),
                                "resistencia_ohm": round(resistencia,2),
                                "velocidad_angular_rad_s": round(rad_s,2)})

    with open(ruta_salida, "w",newline="",encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames= campos)
        escritor.writeheader()
        escritor.writerows(reporte_motores)

if __name__ == "__main__":
    motores =[]
    RUTA_MOTORES = (
    r"C:\Users\AlexisJav\Desktop\DATA SCIENCE"
    r"\01_Python_Basico\motores.csv")
    RUTA_SALIDA = (
    r"C:\Users\AlexisJav\Desktop\DATA SCIENCE\01_Python_Basico\reporte_motores.csv")

    motores =leer_motores(RUTA_MOTORES)
    mostrar_motores(motores)
    mostrar_analisis_motores(motores)
    mostrar_estadisticas_motores(motores)
    mostrar_estadisticas_motores([])
    guardar_reporte_csv(motores, RUTA_SALIDA)
    try:
        guardar_reporte_csv([], RUTA_SALIDA)
    except ValueError as error:
        print(f"Error: {error}")
    try:
        guardar_reporte_csv(motores, "")
    except ValueError as error:
        print(f"Error: {error}")
        