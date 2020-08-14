FROM python:3.8
WORKDIR /app

ADD numbers_to_word /app/service
ADD api /app/api
ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

#RUN ls
#CMD python run.py