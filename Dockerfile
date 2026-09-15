# Imagen base
FROM python:3.12-slim
#evitamops que pyhton cree archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
#Permite visualizar los logs
ENV PYTHONBUFFERED=1
#directorio de trabajo
WORKDIR /app
#dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*
    
#dependencia de python
COPY requirements.txt
#instalamos las dependencias
RUN pip install --no-cache-dir -r requeriments.txt
#codigo de la aplicacion:
COPY . .
#puerto
EXPOSE 5000
#ejecucion
CMD ["gunicorn","--bind","0.0.0.0:5000", "--workers","3","run:app"]