FROM smebberson/alpine-nginx:3.0.0
RUN mkdir -p /etc/log/nginx
RUN mkdir /static
#COPY ./ssl/dhparam.pem /etc/ssl/private/
#COPY ./ssl/ataraxia.io /etc/ssl/ataraxia-lite
COPY ./sites-enabled /etc/nginx/sites-enabled
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/
COPY ./ataraxia-lite-ssl.nginx.conf /etc/nginx/conf.d/
#COPY ./ssl-params.conf /etc/nginx/conf.d/
#COPY ./ssl-ataraxia.io.conf /etc/nginx/conf.d/
COPY ./uwsgi_params /etc/nginx/uwsgi_params
WORKDIR /data/letsencrypt
#RUN mkdir -p .well-known/acme-challenge
#RUN touch /data/letsencrypt/.well-known/acme-challenge/ok.txt
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /etc/log/nginx/access.log
RUN ln -sf /dev/stderr /etc/log/nginx/error.log
