FROM python:3.8-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --upgrade pip && \
    pip3 install python-dotenv && \
    pip3 install -U -r requirements.txt# Actualizar pip e instalar dependencias de Python

COPY . .

CMD ["python3", "main.py"]
