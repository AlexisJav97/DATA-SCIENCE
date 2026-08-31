

def calcular_potencia(voltaje, corriente):
    potencia = voltaje * corriente
    return potencia


def calcular_resistencia(voltaje, corriente):
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