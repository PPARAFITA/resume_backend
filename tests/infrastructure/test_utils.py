# tests/test_utils.py
import pytest
from datetime import date
from src.infrastructure.utils import parse_date  # Cambia esta ruta según tu estructura

# Casos válidos para las fechas
@pytest.mark.parametrize("date_str, expected_date", [
    ("28/10/2021", date(2021, 10, 28)),  # Formato %d/%m/%Y
    ("28-10-2021", date(2021, 10, 28)),  # Formato %d-%m-%Y
    ("2021/10/28", date(2021, 10, 28)),  # Formato %Y/%m/%d
    ("2021-10-28", date(2021, 10, 28)),  # Formato %Y-%m-%d
    ("10/28/2021", date(2021, 10, 28)),  # Formato %m/%d/%Y (formato EE. UU.)
    ("Oct 28, 2021", date(2021, 10, 28)),  # Formato %b %d, %Y
    ("October 28, 2021", date(2021, 10, 28)),  # Formato %B %d, %Y
])
def test_parse_date_valid(date_str, expected_date):
    assert parse_date(date_str) == expected_date

# Caso inválido: Formato no reconocido
def test_parse_date_invalid():
    with pytest.raises(ValueError):
        parse_date("2021-28-10")  # Un formato que no existe en la lista de formatos
