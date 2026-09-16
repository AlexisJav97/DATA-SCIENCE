
"""
Módulo de cálculos eléctricos relacionados con motores.

Responsabilidad:
    Realizar cálculos eléctricos básicos.

Funciones principales:
    - calcular_potencia()
    - calcular_resistencia()
Dependencias:
    Ninguna.
"""


def calcular_potencia(voltaje:float, corriente:float)->float:
    """
    Calcula la potencia [W] del motor con los valores de Voltaje [V] y Corriente [A]

    Paràmetros:
        voltaje: voltaje [V]
        corriente: corriente [A]

    Retorna:
        potencia: potencia [W]

    Excepciones:
        ValueError: si el voltaje o la corriente son negativos.
    """
    if voltaje < 0 or corriente < 0:
        raise ValueError(" el voltaje o corriente necesita ser mayor o igual a 0 ")

    potencia = voltaje * corriente
    return potencia


def calcular_resistencia(voltaje:float, corriente:float)->float:
    """
    Mediante la ley de OHM calcula la resistencia del motor con los valores de Voltaje [V] y Corriente [A]


    Paràmetros:
        voltaje: voltaje [V]
        corriente: corriente [A]

    Retorna:
        resistencia: resistencia [ohms]

    Excepciones:
        ValueError: cuando el voltaje o corriente son menores a cero
        ZeroDivisionError:  cuando la corriente es cero
    """
    if voltaje < 0 or corriente < 0:
        raise ValueError(" el voltaje o corriente necesita ser mayor o igual a 0 ")


    resistencia = voltaje / corriente
    return resistencia

if __name__ == "__main__":
    voltaje = 24
    corriente = 3.2

    potencia = calcular_potencia(voltaje, corriente)
    resistencia = calcular_resistencia(voltaje, corriente)

    print("PRUEBA DEL MÓDULO")
    print(f"Potencia: {potencia:.2f} W")
    print(f"Resistencia: {resistencia:.2f} ohm")
