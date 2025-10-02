FROM python:3.12-slim

# Встановлення Chrome і ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Встановлення allure (опціонально)
RUN curl -o allure-2.23.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.23.0/allure-commandline-2.23.0.tgz \
    && tar -zxvf allure-2.23.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.23.0/bin/allure /usr/bin/allure \
    && rm allure-2.23.0.tgz

WORKDIR /usr/workspace

# Копіюємо requirements.txt
COPY requirements.txt .

# Ставимо залежності Python
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект
COPY . .

CMD ["pytest", "-v", "--alluredir=allure-results"]
