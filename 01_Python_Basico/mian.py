from herramientas.lector_motores import leer_motores
from herramientas.analisis_motor import analizar_motor

RUTA_MOTORES = (
    r"C:\Users\AlexisJav\Desktop\DATA SCIENCE"
    r"\01_Python_Basico\motores.csv"
)

def main() -> None:
    motores = leer_motores(RUTA_MOTORES)

    print("=== ANÁLISIS DE MOTORES ===")
    print()

    for motor in motores:
        potencia, resistencia, velocidad_rad_s = analizar_motor(motor['voltaje'],motor['corriente'],motor['rpm'])

        print(f"Motor: {motor['id']}")
        print(f"Voltaje: {motor['voltaje']:.2f} V")
        print(f"Corriente: {motor['corriente']:.2f} A")
        print(f"RPM: {motor['rpm']}")
        print(f"Potencia: {potencia:.2f} W")
        print(f"Resistencia: {resistencia:.2f} ohm")
        print(f"Velocidad angular: {velocidad_rad_s:.2f} rad/s")
        print(30 * "-")

if __name__ == "__main__":
    main()