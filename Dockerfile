FROM python:3.11

USER 0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

RUN chmod a+x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]