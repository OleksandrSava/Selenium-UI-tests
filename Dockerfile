FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    xvfb \
    default-jre \
    curl \
    unzip \
    tar \
    bash \
    gnupg \
    tzdata \
    fonts-liberation \
    xdg-utils \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -o /tmp/allure-2.14.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.14.0/allure-commandline-2.14.0.tgz \
    && tar -zxvf /tmp/allure-2.14.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.14.0/bin/allure /usr/bin/allure \
    && rm /tmp/allure-2.14.0.tgz

WORKDIR /usr/workspace
COPY requirements.txt /usr/workspace/
RUN pip install --no-cache-dir -r requirements.txt

ENV CHROME_BIN=/usr/bin/chromium
ENV DISPLAY=:99

CMD ["pytest", "-sv", "--alluredir=allure-results"]
