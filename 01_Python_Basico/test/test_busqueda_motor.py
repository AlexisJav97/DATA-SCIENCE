from herramientas.busqueda_motor import (
    buscar_motor_por_id,
    filtrar_motores_por_rpm_minima,
)


def test_busqueda_encontrada() -> None:
    motores = [
        {
            "id": "M1",
            "voltaje": 24.0,
            "corriente": 3.2,
            "rpm": 1500,
        },
        {
            "id": "M2",
            "voltaje": 24.0,
            "corriente": 5.2,
            "rpm": 1600,
        },
    ]

    motor_id_buscado = "M1"
    resultado_esperado = {
        "id": "M1",
        "voltaje": 24.0,
        "corriente": 3.2,
        "rpm": 1500,
    }

    resultado_obtenido = buscar_motor_por_id(motores, motor_id_buscado)

    assert resultado_obtenido == resultado_esperado


def test_busqueda_no_encontrada() -> None:
    motores = [
        {
            "id": "M1",
            "voltaje": 24.0,
            "corriente": 3.2,
            "rpm": 1500,
        },
        {
            "id": "M2",
            "voltaje": 24.0,
            "corriente": 5.2,
            "rpm": 1600,
        },
    ]

    motor_id_buscado = "S32"

    resultado_obtenido = buscar_motor_por_id(motores, motor_id_buscado)

    assert resultado_obtenido is None


def test_filtro_con_varias_coincidencias() -> None:
    motores = [
        {
            "id": "M1",
            "voltaje": 24.0,
            "corriente": 3.2,
            "rpm": 1500,
        },
        {
            "id": "M2",
            "voltaje": 24.0,
            "corriente": 5.2,
            "rpm": 1600,
        },
    ]

    rpm_min = 666

    resultado_esperado = [
        {
            "id": "M1",
            "voltaje": 24.0,
            "corriente": 3.2,
            "rpm": 1500,
        },
        {
            "id": "M2",
            "voltaje": 24.0,
            "corriente": 5.2,
            "rpm": 1600,
        },
    ]

    resultado_obtenido = filtrar_motores_por_rpm_minima(motores, rpm_min)

    assert resultado_obtenido == resultado_esperado


def test_filtro_con_una_coincidencia() -> None:
    motores = [
        {
            "id": "M1",
            "voltaje": 24.0,
            "corriente": 3.2,
            "rpm": 1500,
        },
        {
            "id": "M2",
            "voltaje": 24.0,
            "corriente": 5.2,
            "rpm": 1600,
        },
    ]

    rpm_min = 1550

    resultado_esperado = [
        {
            "id": "M2",
            "voltaje": 24.0,
            "corriente": 5.2,
            "rpm": 1600,
        },
    ]

    resultado_obtenido = filtrar_motores_por_rpm_minima(motores, rpm_min)

    assert resultado_obtenido == resultado_esperado


def test_filtro_con_cero_coincidencias() -> None:
    motores = [
        {
            "id": "M1",
            "voltaje": 24.0,
            "corriente": 3.2,
            "rpm": 1500,
        },
        {
            "id": "M2",
            "voltaje": 24.0,
            "corriente": 5.2,
            "rpm": 1600,
        },
    ]

    rpm_min = 1800

    resultado_esperado = []

    resultado_obtenido = filtrar_motores_por_rpm_minima(motores, rpm_min)

    assert resultado_obtenido == resultado_esperado


def test_filtro_con_igualdad_exacta() -> None:
    motores = [
        {
            "id": "M1",
            "voltaje": 24.0,
            "corriente": 3.2,
            "rpm": 1500,
        },
        {
            "id": "M2",
            "voltaje": 24.0,
            "corriente": 5.2,
            "rpm": 1600,
        }
    ]

    rpm_min = 1600

    resultado_esperado = [
        {
            "id": "M2",
            "voltaje": 24.0,
            "corriente": 5.2,
            "rpm": 1600,
        }
    ]

    resultado_obtenido = filtrar_motores_por_rpm_minima(motores, rpm_min)

    assert resultado_obtenido == resultado_esperado


def test_filtro_con_lista_vacia() -> None:
    motores = []

    rpm_min = 1600

    resultado_esperado = []

    resultado_obtenido = filtrar_motores_por_rpm_minima(motores, rpm_min)

    assert resultado_obtenido == resultado_esperado
