"""
Módulo encargado de realizar el análisis completo de un motor.

Responsabilidad:
    Combinar cálculos eléctricos y conversiones para obtener
    diferentes parámetros de un motor.

Funciones principales:
    - analizar_motor()
    - estadistica_motores()

Dependencias internas:
    - calculos_motor.py
    - conversion.py
    - lector_motores.py

Flujo:
    analizar_motor()
        ├── calcular_potencia()
        ├── calcular_resistencia()
        └── rpm_a_rad_s()
"""

from .calculos_motor import calcular_potencia, calcular_resistencia
from .conversion import rpm_a_rad_s
from .lector_motores import leer_motores

def analizar_motor(voltaje: float,corriente: float ,rpm: int) -> tuple[float,float,float]:
    """
    Analiza las principales variables de un motor.

    Parámetros:
        voltaje: Voltaje del motor en V.
        corriente: Corriente del motor en A.
        rpm: Velocidad del motor en RPM.

    Retorna:
        Tupla en el siguiente orden:
        1. potencia [W]
        2. resistencia [ohm]
        3. velocidad angular [rad/s]
    """

    potencia = calcular_potencia(voltaje, corriente)
    resistencia = calcular_resistencia(voltaje, corriente)

    velocidad_rad = rpm_a_rad_s(rpm)

    return potencia, resistencia, velocidad_rad



def estadistica_motores(motores: list[dict]) -> dict[str, int | float | str]:
    """
    Calcula las estadísticas generales de una lista de motores.

    Parámetros:
        motores: 
        Lista de diccionarios que contiene la información
        de los motores con la siguiente estructura:

            {
                "id": str,
                "voltaje": float,
                "corriente": float,
                "rpm": int
            }

    Retorna:
        Diccionario con las estadísticas calculadas:

            {
                "total_motores": int,
                "voltaje_promedio": float,
                "corriente_promedio": float,
                "rpm_promedio": float,
                "potencia_promedio": float,
                "motor_mayor_potencia": str,
                "potencia_maxima": float,
                "motor_menor_potencia": str,
                "potencia_minima": float
            }

    Excepciones:
            ValueError: Si la lista de motores está vacía.
    """

    if not motores:
        raise ValueError("No existen motores para calcular estadísticas.")
    
    cantidad_motores = 0
    total_voltaje =0
    total_corriente =0
    total_rpm= 0
    total_potencia = 0
    mayor_potencia = float('-inf')
    mayor_motor = ""
    menor_potencia = float('inf')
    menor_motor = ""

    for motor in motores:
        total_voltaje = total_voltaje + motor['voltaje']
        total_corriente = total_corriente + motor['corriente']
        total_rpm = total_rpm + motor['rpm']
        potencia =  calcular_potencia(motor['voltaje'], motor['corriente'])
        total_potencia = total_potencia + potencia
        cantidad_motores = cantidad_motores + 1

        if potencia > mayor_potencia:
            mayor_potencia = potencia
            mayor_motor = motor['id']

        if potencia < menor_potencia:
            menor_potencia = potencia
            menor_motor = motor['id']

    promedio_voltaje = total_voltaje/cantidad_motores
    promedio_corriente = total_corriente/cantidad_motores
    promedio_rpm = total_rpm/cantidad_motores
    promedio_potencia = total_potencia/cantidad_motores

    return {"total_motores":cantidad_motores,
            "voltaje_promedio": promedio_voltaje,
            "corriente_promedio": promedio_corriente,
            "rpm_promedio": promedio_rpm,
            "potencia_promedio": promedio_potencia,
            "motor_mayor_potencia": mayor_motor,
            "potencia_maxima": mayor_potencia,
            "motor_menor_potencia": menor_motor,
            "potencia_minima": menor_potencia}


if __name__ == "__main__":
    potencia, resistencia, velocidad_rad_s = analizar_motor(voltaje=48, corriente= 4, rpm=1800)

    print(f"PRUEBA DE analisis_motor")
    print(f"POTENCIA: {potencia:.2f} W")
    print(f"RESISTENCIA: {resistencia:.2f} ohm")
    print(f"VELOCIDAD ANGULAR: {velocidad_rad_s:.2f} rad/s")

    ruta = r"C:\Users\AlexisJav\Desktop\DATA SCIENCE\01_Python_Basico\motores.csv"

    motores = leer_motores(ruta)
    print(estadistica_motores(motores))
    try:
        estadistica_motores([])

    except ValueError as error:
        print(f"Error: {error}")

    print(estadistica_motores([{
            "id": "M0",
            "voltaje": 0,
            "corriente": 0,
            "rpm": 0
        }]))

