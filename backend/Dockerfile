FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r \ 
    requirements.txt \
    flask-restful \
    pipenv \
    psycopg2-binary

COPY app/ .

WORKDIR /

COPY main.py .

ENV export FLASK_APP="main:app"
ENV export FLASK_ENV="development"

CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
# CMD ["python3", "main.py"]