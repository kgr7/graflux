FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update
RUN apt-get install iputils-ping -y

COPY . .

CMD ["python3", "main.py"]