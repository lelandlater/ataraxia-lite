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
