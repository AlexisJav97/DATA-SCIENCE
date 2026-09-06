"""
Módulo encargado de realizar búsquedas específicas de motores.

Responsabilidad:
    - Buscar motores mediante criterios específicos.
    - Filtrar motores que cumplan una condición.

Funciones principales:
    - buscar_motor_por_id()
    - filtrar_motores_por_rpm_minima()

Dependencias:
    - lector_motores.py
      Solo se utiliza para la prueba interna del módulo.

Usado por:
    - main.py
"""
from .lector_motores import leer_motores

def buscar_motor_por_id(motores: list[dict], motor_id: str) -> dict|None:
    """
    Busca un motor mediante su identificador.

    Parámetros:
        motores:
            Lista de diccionarios con los motores disponibles.

        motor_id:
            Identificador del motor que se desea buscar.

    Retorna:
        Diccionario con los datos del motor si fue encontrado.
        
        Ejemplo:
            {
                "id": "M1",
                "voltaje": 24.0,
                "corriente": 3.2,
                "rpm": 1500
            }

        None:
            Si no existe un motor con el ID especificado.
    """
    for motor in motores:
        if motor["id"] == motor_id:
            return motor
    return None

def filtrar_motores_por_rpm_minima(motores: list[dict], rpm_min: int) -> list[dict[str, int|float|str]]:
    """
    Filtra los motores cuya velocidad es igual o superior
    a una cantidad mínima de RPM.

    Parámetros:
        motores:
            Lista de diccionarios con los motores disponibles.

            Ejemplo de estructura:

                {
                    "id": "M1",
                    "voltaje": 24.0,
                    "corriente": 3.2,
                    "rpm": 1500
                }

        rpm_minima:
            Velocidad mínima en RPM que debe tener un motor
            para ser incluido en el resultado.

    Retorna:
        Lista de diccionarios con los motores cuya velocidad
        es igual o superior a rpm_minima.

        Retorna una lista vacía si ningún motor cumple
        la condición o si la lista recibida está vacía.
    """
    motores_rpm_min = []
    for motor in motores:
        if motor['rpm'] >= rpm_min:
            motores_rpm_min.append(motor)

    return motores_rpm_min



if __name__ == "__main__":
    RUTA_MOTORES = (
    r"C:\Users\AlexisJav\Desktop\DATA SCIENCE"
    r"\01_Python_Basico\motores.csv")
    motores = leer_motores(RUTA_MOTORES)
    print(buscar_motor_por_id(motores, "M1"))
    print(filtrar_motores_por_rpm_minima(motores,1400))

    print(filtrar_motores_por_rpm_minima([],1400))
    print(filtrar_motores_por_rpm_minima(motores, 1400))
    print(filtrar_motores_por_rpm_minima(motores, 1450))
    print(filtrar_motores_por_rpm_minima(motores, 5000))
    print(filtrar_motores_por_rpm_minima([], 1400))
    
