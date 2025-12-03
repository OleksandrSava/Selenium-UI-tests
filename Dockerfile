FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    ALLURE_VERSION=2.27.0

RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver \
    nss \
    udev \
    harfbuzz \
    freetype \
    ttf-freefont \
    font-noto \
    curl \
    tar \
    bash \
    openjdk17-jre

RUN curl -sLo /tmp/allure.tgz "https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz" \
    && mkdir -p /opt \
    && tar -xzf /tmp/allure.tgz -C /opt \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure \
    && rm /tmp/allure.tgz \
    && allure --version

WORKDIR /usr/workspace

COPY requirements.txt /usr/workspace/requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install pytest selenium allure-pytest

COPY . /usr/workspace