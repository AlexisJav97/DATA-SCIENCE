from herramientas.analisis_motor import analizar_motor


def main():

    voltaje = 24
    corriente = 3.2
    rpm = 1500

    potencia, resistencia, velocidad_rad = analizar_motor(
        voltaje,
        corriente,
        rpm
    )

    print("ANÁLISIS DEL MOTOR")
    print("--------------------")
    print(f"Voltaje: {voltaje:.2f} V")
    print(f"Corriente: {corriente:.2f} A")
    print(f"RPM: {rpm}")
    print(f"Potencia: {potencia:.2f} W")
    print(f"Resistencia: {resistencia:.2f} ohm")
    print(f"Velocidad angular: {velocidad_rad:.2f} rad/s")


if __name__ == "__main__":
    main()