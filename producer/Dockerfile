FROM python:3.8-slim


RUN apt-get update
RUN apt-get install -y build-essential 

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python","-u","main.py"]