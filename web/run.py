from flask import Flask, render_template, url_for
from htmlmin.minify import html_minify

app = Flask(__name__)
app.config['SERVER_NAME'] = 'ataraxialocal'

"""ATARAXIA in Greek."""
ataraxia = '&#x3AC;&#x3C4;&#x3B1;&#x3C1;&#x3B1;&#x3BE;&#x3AF;&#x3B1;'

"""For navigation bar."""
class NavItem(object):

    def __init__(self, url, label, homelogo=False):
        self.func_url = url
        self.label = label
        self.homelogo = homelogo

@app.route('/')
@app.route('/index')
def index():
	nav = [NavItem(url_for('index'), ataraxia.encode('unicode-escape'), True),
           NavItem(url_for('contact'), 'CONTACT')]
	rendered = render_template('index.html', navitems=nav)
	return html_minify(rendered)

@app.route('/contact')
def contact():
	nav = [NavItem(url_for('index'), ataraxia.encode('unicode-escape'), True)]
	rendered = render_template('contact.html', navitems=nav)
	return html_minify(rendered)

if __name__=='__main__':
	app.run(port=9000, debug=True, use_reloader=False)
