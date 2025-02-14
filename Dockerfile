FROM python:3.8-slim

WORKDIR /cc-chk-bot

# Instalar dependencias del sistema necesarias

COPY requirements.txt

# Actualizar pip e instalar las dependencias de Python
RUN pip install --upgrade pip && \
    pip install -U -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando para ejecutar la aplicación
CMD ["python3", "run.py"]
