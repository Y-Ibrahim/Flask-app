
FROM python:3.8-slim-buster
WORKDIR /Python_Blog
COPY requirements.txt requirements.txt
# Install system dependencies required by mysqlclient
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev  gcc\
    && pip install -r requirements.txt \
    && pip install mysqlclient
COPY . /Python_Blog
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
