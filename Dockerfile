FROM debian

RUN apt-get -qq update
RUN apt-get install -y python python-pip

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app.py
