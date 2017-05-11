FROM smebberson/alpine-nginx:3.0.0
RUN mkdir -p /etc/ssl/ataraxia-lite
RUN mkdir -p /etc/log/nginx
RUN mkdir /static
COPY ./ssl/dhparam.pem /etc/ssl/ataraxia-lite
COPY ./ssl/ataraxia.io /etc/ssl/ataraxia-lite
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/
COPY ./ataraxia-lite-ssl.nginx.conf /etc/nginx/conf.d/
COPY ./uwsgi_params /etc/nginx/uwsgi_params
 
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /etc/log/nginx/access.log
RUN ln -sf /dev/stderr /etc/log/nginx/error.log

