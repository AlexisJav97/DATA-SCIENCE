"""
Módulo de cálculos eléctricos relacionados con motores.

Responsabilidad:
    Realizar cálculos eléctricos básicos.

Funciones principales:
    - calcular_potencia()
    - calcular_resistencia()

Dependencias:
    Ninguna.
"""

def rpm_a_rad_s(rpm: int) -> float:
    """
    Convierte de RPM -> rad/s    
    
    Paràmetros:
        rpm
    Retorna:
        rad/s
    """
    rad_s = rpm*2*3.1416/60
    return rad_s