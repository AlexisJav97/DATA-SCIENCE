from herramientas import (calcular_resistencia, calcular_potencia, rpm_a_rad_s)

voltaje = 99
corriente = 3.2
rpm = 1500

potencia= calcular_potencia(voltaje, corriente)

resistencia = calcular_resistencia(voltaje, corriente)

velocidad_rad = rpm_a_rad_s(rpm)


print(f"Potencia: {potencia:.2f} W")
print(f"Resistencia: {resistencia:.2f} ohm")
print(f"Velocidad angular: {velocidad_rad:.2f} rad/s")
