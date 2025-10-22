# ---------- DOCKERFILE OTIMIZADO PARA RENDER ----------
# Força Python 3.12 slim, compatível com FastAPI + pandas binário
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Define variáveis para evitar interações e acelerar build
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Copia os arquivos de requisitos primeiro (melhor cache)
COPY requirements.txt .

# Instala dependências do sistema necessárias pro pandas e FastAPI
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    libssl-dev \
    curl \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Copia o restante do backend
COPY . .

# Expõe a porta que o Render usa automaticamente
ENV PORT=10000

# Comando de inicialização
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
