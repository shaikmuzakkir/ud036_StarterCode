import webbrowser

class Movie():
	""" This class defines the attributes and methods every intsnace of a Movie class should have."""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	# This mehtod shows hte trailers of the instantiated movie object
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)