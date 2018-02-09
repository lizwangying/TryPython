import webbrowser
class Movie(object):
	"""docstring for movie"""
	def __init__(self, title,trailer_youtube_id,poster_image_url,trailer_youtube_url):
		super(Movie, self).__init__()
		self.title = title
		self.trailer_youtube_id = trailer_youtube_id
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
	
	def show_trailer(self):
		webbrowser.open(trailer_youtube_url)



		