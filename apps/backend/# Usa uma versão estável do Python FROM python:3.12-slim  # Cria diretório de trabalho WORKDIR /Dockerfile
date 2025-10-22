# Usa uma versão estável do Python
FROM python:3.12-slim

# Cria diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe a porta padrão usada pelo Render ($PORT)
ENV PORT=10000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
