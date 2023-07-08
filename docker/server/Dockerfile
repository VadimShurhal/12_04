FROM python:3.11-alpine

WORKDIR /server

COPY . /server

RUN pip install -r requirements.txt && apk --no-cache add curl

CMD ["python3", "server.py"]



