FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    wget unzip gnupg curl chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Define variáveis
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH=$PATH:/usr/bin/chromium

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . /app
WORKDIR /app

CMD ["python", "scraper.py"]