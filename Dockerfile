# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de la aplicación al contenedor
COPY . /app/

# Exponer el puerto en el que la aplicación Flask corre (5000 por defecto)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
