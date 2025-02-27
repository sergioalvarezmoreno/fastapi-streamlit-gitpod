#!/bin/bash

# Iniciar la API en segundo plano
echo "Iniciando la API FastAPI..."
python -m uvicorn app:app --host 0.0.0.0 --port 8000 &

# Esperar un momento para que la API se inicie
sleep 5

# Iniciar el frontend de Streamlit
echo "Iniciando el frontend Streamlit..."
python -m streamlit run frontend.py --server.port 8501
