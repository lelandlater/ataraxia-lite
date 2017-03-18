FROM python:3.4.6-onbuild

RUN pip install uwsgi 

EXPOSE 8000