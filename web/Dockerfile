FROM python:3.4.6-onbuild

MAINTAINER Leland Later '<leland@ataraxia.io>'

RUN pip install -r requirements.txt

EXPOSE 5000

CMD uwsgi --ini uwsgi.ini
