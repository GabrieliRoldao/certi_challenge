FROM python:3.8
WORKDIR /app

ADD service /app/service
ADD api /app/api
ADD logger /app/logger
ADD requirements.txt /app/requirements.txt
ADD run.py /app/run.py

RUN pip install -r requirements.txt

CMD python run.py