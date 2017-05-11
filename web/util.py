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
		self._url = url
		self._label = label

		if color is not None:
			self.set_color(color)
		else:
			self._color = None

	def _get_url(self):
		return self._url

	def _get_label(self):
		return self._label

	def _get_color(self):
		return self._color

	# check if color is acceptable hexadecimal value or CSS built-in.
	def set_color(self, color):
		# TODO hex logic
		self._color = color
