from flask import Flask, render_template, url_for
from htmlmin.minify import html_minify
import html.parser
from util import NavBar, NavItem, ContactLink

app = Flask(__name__)
app.config['SERVER_NAME'] = 'ataraxia.io'


"""ATARAXIA in Greek."""
hparser=html.parser.HTMLParser()
ataraxia='&#x3AC;&#x3C4;&#x3B1;&#x3C1;&#x3B1;&#x3BE;&#x3AF;&#x3B1;'
ataraxia=hparser.unescape(ataraxia)

"""Index page displaying logo and link to contact page."""
@app.route('/')
@app.route('/index')
def index():
	nav = NavBar([NavItem(url_for('index'), ataraxia)], [NavItem(url_for('contact'), 'CONTACT')])
	rendered = render_template('index.html', nav=nav)
	return html_minify(rendered)

"""Display contact links and link back to index page."""
@app.route('/contact')
def contact():
	nav = NavBar([NavItem(url_for('index'), ataraxia)], [])
	links = [ContactLink('https://github.com/lelandlater', 'GITHUB', '4078c0'),
	         ContactLink('https://twitter.com/lelandlater', 'TWITTER', '00aced'),
	         ContactLink('https://linkedin.com/lelandlater', 'LINKEDIN', '0077b5'),
	         ContactLink('https://bitbucket.org/lelandlater', 'BITBUCKET', '205081')]
	rendered = render_template('contact.html', nav=nav, links=links)
	return html_minify(rendered)

if __name__=='__main__':
	app.run(port=9000, debug=True, use_reloader=False)
