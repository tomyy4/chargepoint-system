FROM python:3.11

USER 0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

WORKDIR /app

ENV DATABASE_URL=postgresql://${DATABASE_USER}:${DATABASE_PASSWORD}@${DATABASE_HOST}:${DATABASE_PORT}/${DATABASE_NAME}

COPY docker.env /app/.env
COPY src /app/src
COPY requirements.txt /app/requirements.txt
COPY entrypoint.sh /app/entrypoint.sh

RUN pip install -r /app/requirements.txt

RUN chmod a+x /app/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]