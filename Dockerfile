# base image
FROM python:3.11
# setup environment variable

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

WORKDIR /app

COPY . /app
# where your code lives

RUN pip install -r /app/requirements.txt


# port where the Django app runs
EXPOSE 8000
# start server
RUN chmod a+x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]