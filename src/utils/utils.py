from datetime import datetime

DATE_FORMATS = [
    "%d/%m/%Y",  # 28/10/2021
    "%d-%m-%Y",  # 28-10-2021
    "%Y/%m/%d",  # 2021/10/28
    "%Y-%m-%d",  # 2021-10-28
    "%m/%d/%Y",  # 10/28/2021 (formato de EE.UU.)
    "%b %d, %Y",  # Oct 28, 2021
    "%B %d, %Y",  # October 28, 2021
]

def parse_date(date_str: str):
    """ Intenta convertir una fecha en diferentes formatos al formato YYYY-MM-DD """
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Formato de fecha no reconocido: {date_str}")
