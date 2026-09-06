"""
Paquete de herramientas para el análisis de motores.

Módulos:
    lector_motores:
        Lectura y validación de archivos CSV.

    calculos_motor:
        Cálculos eléctricos.

    conversion:
        Conversión de unidades.

    analisis_motor:
        Análisis completo reutilizando cálculos y conversiones.
"""

from .calculos_motor import calcular_potencia, calcular_resistencia
from .conversion import rpm_a_rad_s