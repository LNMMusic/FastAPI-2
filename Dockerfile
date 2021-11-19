FROM python:3.9-slim-buster
WORKDIR /backend

# Dependencies
COPY /requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2==2.9.1

# Network
EXPOSE 8080

# Run
# CMD [ "python", "main.py" ]