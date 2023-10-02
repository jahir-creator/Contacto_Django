#!/bin/bash

# Nombre del proceso que deseas detener (el comando que lo inicia)
PROCESS_NAME="python manage.py runserver 0.0.0.0:8000"

# Buscar y detener el proceso por el nombre del comando
pids=$(pgrep -f "$PROCESS_NAME")
if [ -n "$pids" ]; then
    for pid in $pids; do
        kill "$pid"
    done
    echo "Servidor Django detenido."
else
    echo "El servidor Django ya está detenido o no se encontró el proceso."
fi


