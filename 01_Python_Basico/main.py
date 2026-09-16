from herramientas.lector_motores import leer_motores
from herramientas.reportes import mostrar_motores, mostrar_analisis_motores, mostrar_estadisticas_motores, guardar_reporte_csv
from herramientas.busqueda_motor import buscar_motor_por_id, filtrar_motores_por_rpm_minima
from pathlib import Path

CARPETA_PROYECTO = Path(__file__).resolve().parent

CARPETA_DATOS = CARPETA_PROYECTO / "datos"
CARPETA_REPORTES = CARPETA_PROYECTO / "reportes"

RUTA_MOTORES = CARPETA_DATOS / "motores.csv"
RUTA_REPORTE = CARPETA_REPORTES / "reporte_motores.csv"

def main() -> None:
    try:
        CARPETA_REPORTES.mkdir(parents=True, exist_ok=True)
        motores = leer_motores(RUTA_MOTORES)

    except (TypeError, ValueError) as error:
        print(f"Error en la configuración de la ruta: {error}")
        return

    except OSError as error:
        print(f"Error al preparar los archivos: {error}")
        return

    while True:

        print("=== SISTEMA DE ANÁLISIS DE MOTORES ===")
        print()
        print("""
            1. Mostrar motores
            2. Analizar motores
            3. Buscar motor por ID
            4. Mostrar estadísticas
            5. Filtrar motores
            6. Guardar reporte CSV
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
                rpm_minima = int(
                    input("Ingrese la velocidad mínima del motor en RPM: ")
                )

            except ValueError:
                print("❌ Ingrese un número entero válido para las RPM.")
                continue

            if rpm_minima < 0:
                print("❌ La velocidad mínima no puede ser negativa.")
                continue

            motores_filtrados = filtrar_motores_por_rpm_minima(
                motores,
                rpm_minima
            )

            if not motores_filtrados:
                print(
                    f"No existen motores con una velocidad igual "
                    f"o superior a {rpm_minima} RPM."
                )
            else:
                mostrar_motores(motores_filtrados)

        elif opc_menu == 6:
            try:

                guardar_reporte_csv(motores, RUTA_REPORTE)
                print("✅ Reporte CSV guardado correctamente.")
                print(f"Ubicación: {RUTA_REPORTE}")
            except ValueError as error:
                print(f"Error en los datos: {error}")

            except TypeError as error:
                print(f"Error en la ruta: {error}")

            except OSError as error:
                print(f"Error al guardar el archivo: {error}")
        elif opc_menu == 0:
            print("Finalizando...")
            break    

        else:
            print("Opción inválida")

            

if __name__ == "__main__":
    print(f"Carpeta del proyecto: {CARPETA_PROYECTO}")
    print(5*"----")
    print(f"Carpeta de entrada: {CARPETA_DATOS}")
    print(f"Carpeta de salida: {CARPETA_REPORTES}")
    print(5*"----")
    print(f"Archivo de entrada: {RUTA_MOTORES}")
    print(f"Archivo de salida: {RUTA_REPORTE}")
    print(5*"----")
    print(__file__)
    print(5*"----")
    #__file__       → cadena con una ubicación
    #Path(__file__) → objeto para manipular esa ubicación
    print(type(__file__))
    print(type(Path(__file__)))
    print(5*"$$$$")
    #RUTA ABSOLUTA COMPLETA
    print(Path(__file__).resolve()) 
    print(type(Path(__file__).resolve())) 
    print(5*"@@@@")
    #RUTA DE LA CARPETA QUE CONTIENE ESE ARCHIVO
    print(Path(__file__).resolve().parent)
    print(type(Path(__file__).resolve().parent))
    print(5*"----")

    print("=== COMPROBACIÓN DE RUTAS ===")
    print(f"¿Existe LA RUTA DE motores.csv?: {RUTA_MOTORES.exists()}") #TRUE
    print(f"¿Es un archivo?: {RUTA_MOTORES.is_file()}") #TRUE
    print(f"¿Existe LA RUTA DE la carpeta datos?: {CARPETA_DATOS.exists()}")#TRUE
    print(f"¿Es una carpeta?: {CARPETA_DATOS.is_dir()}") #TRUE
    print(f"¿Existe LA RUTA DE LA carpeta reportes?: {CARPETA_REPORTES.exists()}")
    print(f"¿Es una carpeta?: {CARPETA_REPORTES.is_dir()}")
    main()
