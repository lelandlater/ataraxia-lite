from flask import Flask, render_template, url_for
from htmlmin.minify import html_minify
import HTMLParser

app = Flask(__name__)
app.config['SERVER_NAME'] = 'ataraxialocal'


"""ATARAXIA in Greek."""
hparser=HTMLParser.HTMLParser()
ataraxia='&#x3AC;&#x3C4;&#x3B1;&#x3C1;&#x3B1;&#x3BE;&#x3AF;&#x3B1;'
ataraxia=hparser.unescape(ataraxia)

"""
Generalized navigation. NavBar passed to Jinja, composed of two NavItem lists.
"""

class NavItem(object):

    def __init__(self, url, label):
        self.url = url
        self.label = label

class NavBar(object):
	"""
	Two lists: starting and ending NavItems for use with flexbox layout.
	"""
	def __init__(self, start, end):
		self.start = start
		self.end = end

class ContactLink(object):
	"""
	URL, label, and brand color.
	"""
	def __init__(self, url, label, color=None):
		self.url = url
		self.label = label

		if color is not None:
			set_color(color)
		else:
			self.color = None

	# check if color is acceptable hexadecimal value or CSS built-in.
	def set_color(self, color):
		# TODO hex logic
		self.color = color


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
	nav = NavBar([NavItem(url_for('index'), ataraxia.encode('unicode-escape'))], [NavItem(url_for('contact'), 'CONTACT')])
	rendered = render_template('contact.html', nav=nav)
	return html_minify(rendered)

if __name__=='__main__':
	app.run(port=9000, debug=True, use_reloader=False)
