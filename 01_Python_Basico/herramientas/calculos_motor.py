
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
    """
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
    """
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