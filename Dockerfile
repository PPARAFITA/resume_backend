FROM python:3.9

WORKDIR /app

# Copiar el script wait-for-it.sh
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app_api", "--host", "0.0.0.0", "--port", "8080"]