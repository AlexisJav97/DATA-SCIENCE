from herramientas.lector_motores import leer_motores
from herramientas.reportes import mostrar_motores, mostrar_analisis_motores, mostrar_estadisticas_motores
from herramientas.busqueda_motor import buscar_motor_por_id, filtrar_motores_por_rpm_minima

RUTA_MOTORES = (
    r"C:\Users\AlexisJav\Desktop\DATA SCIENCE"
    r"\01_Python_Basico\motores.csv"
)

def main() -> None:
    motores = leer_motores(RUTA_MOTORES)

    while True:

        print("=== SISTEMA DE ANÁLISIS DE MOTORES ===")
        print()
        print("""
            1. Mostrar motores
            2. Analizar motores
            3. Buscar motor por ID
            4. Mostrar estadísticas
            5. Filtrar motores
            0. Salir
            """)
        try:
            opc_menu = int(input("SELECCIONE UNA OPCIÓN: "))
        except ValueError:
            print("❌ INGRESE UNA OPCIÓN VÁLIDA")
            continue

        if opc_menu == 1:
            mostrar_motores(motores)
                
        elif opc_menu == 2:
            mostrar_analisis_motores(motores)

        elif opc_menu == 3:
            id_motor = input("Ingrese el ID del motor (Ej.: M1): ").strip().upper()
            motor_encontrado = buscar_motor_por_id(motores, id_motor)
            if motor_encontrado is not None:
                mostrar_motores([motor_encontrado])
            else:
                print("❌ Motor no encontrado")

        elif opc_menu == 4:
            mostrar_estadisticas_motores(motores)

        elif opc_menu == 5:
            try:
                motores_filtrados = []
                rpm_minima = int(input("Ingrese la velocidad minima del motor en RPM: "))

            except ValueError:
                print("❌ Ingrese un número entero válido para las RPM.")
                continue

            motores_filtrados = filtrar_motores_por_rpm_minima(motores, rpm_minima)

            if rpm_minima < 0:
                print("❌ La velocidad mínima no puede ser negativa.")
                continue

            if not motores_filtrados:
                print(f"No existen motores con una velocidad igual o superior a {rpm_minima} RPM.")
            else:
                mostrar_motores(motores_filtrados)           

        elif opc_menu == 0:
            print("Finalizando...")
            break    

        else:
            print("Opción inválida")

            

if __name__ == "__main__":
    main()