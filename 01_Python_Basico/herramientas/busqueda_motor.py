"""
Módulo encargado de realizar búsquedas específicas de motores.

Responsabilidad:
    - Buscar un motor mediante su identificador.

Funciones principales:
    - buscar_motor_por_id()

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



if __name__ == "__main__":
    RUTA_MOTORES = (
    r"C:\Users\AlexisJav\Desktop\DATA SCIENCE"
    r"\01_Python_Basico\motores.csv")
    motores = leer_motores(RUTA_MOTORES)
    print(buscar_motor_por_id(motores, "M1"))
    
