import pytest

from herramientas.calculos_motor import calcular_potencia, calcular_resistencia

def test_calcular_potencia() -> None:
    voltaje = 24
    corriente = 3.2
    potencia_esperada = 76.8

    potencia_obtenida = calcular_potencia(voltaje, corriente)

    assert potencia_obtenida == pytest.approx(potencia_esperada)

def test_calcular_potencia_corriente_cero() -> None:
    voltaje = 24
    corriente = 0
    potencia_esperada = 0

    potencia_obtenida = calcular_potencia(voltaje, corriente)

    assert potencia_obtenida == pytest.approx(potencia_esperada)

def test_calcular_potencia_dos_decimales() -> None:
    voltaje = 64
    corriente = 7.31
    potencia_esperada = 467.84

    potencia_obtenida = calcular_potencia(voltaje, corriente)

    assert potencia_obtenida == pytest.approx(potencia_esperada)

def test_calcular_resistencia() -> None:
    voltaje = 4
    corriente = 78.6727
    resistencia_esperada = 0.05084355818

    resistencia_obtenida = calcular_resistencia(voltaje, corriente)

    assert resistencia_obtenida == pytest.approx(resistencia_esperada)

def test_calcular_resistencia_con_corriente_cero() -> None:

    voltaje = 4
    corriente = 0

    with pytest.raises(ZeroDivisionError):
        calcular_resistencia(voltaje, corriente)

def test_calcular_potencia_con_voltaje_negativo() -> None:

    voltaje = -67
    corriente = 2.45


    with pytest.raises(ValueError):
        calcular_potencia(voltaje, corriente)

def test_calcular_potencia_con_corriente_negativa() -> None:

    voltaje = 30
    corriente = -60

    with pytest.raises(ValueError):
        calcular_potencia(voltaje, corriente)

def test_calcular_resistencia_con_voltaje_negativo() -> None:
    voltaje = -50
    corriente = 23

    with pytest.raises(ValueError):
        calcular_resistencia(voltaje, corriente)

def test_calcular_resistencia_con_corriente_negativa() -> None:
    voltaje = 20
    corriente = -2.57

    with pytest.raises(ValueError):
        calcular_resistencia(voltaje, corriente)
