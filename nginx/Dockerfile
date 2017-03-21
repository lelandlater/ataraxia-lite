FROM smebberson/alpine-base:3.0.0
RUN mkdir /etc/ssl/ataraxia-lite
#COPY ./ssl/dhparams.pem /etc/ssl/ataraxia-lite
#COPY ./ssl/ataraxia.io /etc/ssl/ataraxia-lite
COPY ./sites-enabled /etc/nginx/sites-enabled
COPY ./nginx.conf /etc/nginx/
COPY ./ataraxia-lite.nginx.conf /etc/nginx/conf.d/
#RUN rm /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

# forward request and error logs to docker log collector
# RUN ln -sf /dev/stdout /var/log/nginx/access.log
# RUN ln -sf /dev/stderr /var/log/nginx/error.log # TODO: look at apline logs

