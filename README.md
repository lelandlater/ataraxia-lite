# ataraxia-lite
[ataraxia.io](https://ataraxia.io) hosts Leland Later's projects. This iteration of ataraxia.io displays a home page and contact information with minimal static resources and a simple server configuration.

### Application
_ataraxia-lite_ is written in Python using the [Flask](http://flask.pocoo.org) web development framework. The application is served with [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/), an implementation of the WSGI protocol, which is a Python interface between web servers and web applications.

### Server 
_ataraxia-lite_ serves HTTPS traffic with [NGINX](https://www.nginx.com/resources/wiki/).

### Infrastructure
_ataraxia-lite_ runs on a very small [EC2 instance on Amazon Web Services](https://aws.amazon.com/ec2/). The site leverages Docker and Docker Compose to containerize and run processes in logical isolation.

##### Contact
Reach Leland Later at [ataraxia.io/contact](https://ataraxia.io/contact).
