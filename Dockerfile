FROM python:2.7
COPY requirements.txt /code/requirements.txt
WORKDIR /code
EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python", "manage.py","runserver","0.0.0.0:8000","--noreload"]