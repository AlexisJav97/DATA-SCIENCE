herramientas/
│
├── README.md              ← mapa del paquete
├── __init__.py
├── analisis_motor.py
├── calculos_motor.py
├── conversion.py
└── lector_motores.py

# Paquete herramientas

Contiene las funciones utilizadas para leer, validar,
convertir y analizar datos de motores.

## Estructura

| Módulo | Responsabilidad |
|---|---|
| lector_motores.py | Leer y validar motores desde CSV |
| calculos_motor.py | Cálculos eléctricos |
| conversion.py | Conversión de unidades |
| analisis_motor.py | Coordinar el análisis completo |

## Dependencias internas

main.py
    |
    +-- lector_motores.py
    |
    +-- analisis_motor.py
            |
            +-- calculos_motor.py
            |
            +-- conversion.py