FROM python:3.10-alpine AS builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -U pip setuptools wheel && \
    pip wheel \
    --no-cache-dir \
    --no-deps \
    --wheel-dir /app/wheels \
    -r requirements.txt

FROM python:3.10.3-slim-buster

ENV HOME=/home/rishat
ENV APP_HOME=/home/rishat/app
ENV PYTHONUNBUFFERED 1
RUN mkdir -p $HOME && \
    mkdir $APP_HOME && \
    addgroup --system --gid 1000 rishat_app && \
    adduser --system --gid 1000 --uid 1000 rishat_app

WORKDIR $APP_HOME

COPY --from=builder /app/wheels /wheels

RUN pip install --no-cache-dir -U pip wheel setuptools && \
    pip install --no-cache-dir /wheels/*

COPY . .
RUN chown -R 1000:1000 . && chmod +x ./scripts/*.sh

USER rishat_app

ENTRYPOINT ["./scripts/run.sh"]