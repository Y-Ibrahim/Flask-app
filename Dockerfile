
FROM python:3.8-slim-buster
WORKDIR /Python_Blog
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt \
    pip install flask_sqlalchemy \
    pip install flask_login
COPY . /Python_Blog
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

