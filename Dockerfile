FROM python:3.12-slim

# Встановлюємо Chromium для headless тестів
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    fonts-liberation \
    wget \
    curl \
    unzip \
    tzdata \
    ca-certificates \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/workspace

# Встановлюємо Python-залежності
COPY ./requirements.txt /usr/workspace
RUN pip install --no-cache-dir -r requirements.txt
