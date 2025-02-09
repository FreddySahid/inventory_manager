# logging_config.py
import logging
import os
from datetime import datetime

# Crear la carpeta de logs si no existe
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configurar el formato del log
log_format = "%(asctime)s - %(filename)s - %(levelname)s - %(message)s"

# Configurar el manejador de archivo
file_handler = logging.FileHandler(f"logs/app.log")
file_handler.setFormatter(logging.Formatter(log_format))

# Configurar el logger principal
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)