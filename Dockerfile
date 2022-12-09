FROM python:3.10.7

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install  -r requirements.txt

ENV PIP_ROOT_USER_ACTION=ignore

EXPOSE 8000

CMD ["python", "app.py"]
