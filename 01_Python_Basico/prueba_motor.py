import calculos_motor as calcMotor

voltaje = 24
corriente = 3.2

potencia= calcMotor.calcular_potencia(voltaje, corriente)

resistencia = calcMotor.calcular_resistencia(voltaje, corriente)

print(f"Potencia: {potencia:.2f} W")
print(f"Resistencia: {resistencia:.2f} ohm")