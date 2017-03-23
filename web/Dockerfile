FROM python:3.4.6-onbuild

MAINTAINER Leland Later '<leland@ataraxia.io>'

RUN pip install -r requirements.txt

CMD uwsgi --ini uwsgi.ini

# all the python goes to usr/src/app