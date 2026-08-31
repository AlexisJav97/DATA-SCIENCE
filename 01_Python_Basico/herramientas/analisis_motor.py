from .calculos_motor import calcular_potencia, calcular_resistencia
from .conversion import rpm_a_rad_s

def analizar_motor(voltaje,corriente,rpm):
    potencia = calcular_potencia(voltaje, corriente)
    resistencia = calcular_resistencia(voltaje, corriente)

    velocidad_rad = rpm_a_rad_s(rpm)

    return potencia, resistencia, velocidad_rad

if __name__ == "__main__":
    potencia, resistencia, velocidad_rpm = analizar_motor(voltaje=48, corriente= 4, rpm=1800)

    print(f"PRUEBA DE analisis_motor")
    print(f"POTENCIA: {potencia:.2f} W")
    print(f"RESISTENCIA: {resistencia:.2f} ohm")
    print(f"VELOCIDAD ANGULAR: {velocidad_rpm:.2f} rad/s")

