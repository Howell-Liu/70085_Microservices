FROM ubuntu
RUN apt update && apt install -y python3 python3-pip

RUN mkdir /usr/share/flask-app
COPY . /usr/share/flask-app

WORKDIR /usr/share/flask-app
RUN pip install -r requirements.txt

CMD ["flask", "--app", "app", "run", "--host", "0.0.0.0"]

