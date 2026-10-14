# SIPSIXA

Portal web del programa académico (proyecto universitario). Flask + MySQL + Docker.

## Cómo ejecutarlo

1. Copia `.env.example` como `.env` y cambia las contraseñas.
2. Abre Docker Desktop y, en esta carpeta, ejecuta:

   ```
   docker compose up --build
   ```
3. Abre http://localhost:5000
4. Comprobaciones: http://localhost:5000/salud (app) y http://localhost:5000/salud/db (base de datos).

Para apagar: `docker compose down`. Para borrar también los datos de MySQL: `docker compose down -v`.

## Estructura

```
app/
  controllers/  models/  repositories/  routes/  schemas/  services/
  templates/ (base.html, index.html, partials/)
  static/ (css, js, img)
  __init__.py  config.py  extensions.py
run.py  Dockerfile  docker-compose.yml  requirements.txt
```
