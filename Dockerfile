# Imagen base
FROM python:3.12-slim

# evitamos que python cree archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# permite visualizar los logs
ENV PYTHONUNBUFFERED=1

# directorio de trabajo
WORKDIR /app

# dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# dependencias de python
COPY requirements.txt .
# instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# codigo de la aplicacion
COPY . .

# puerto
EXPOSE 5000

# ejecucion
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "run:app"]
