# -*- coding=UTF-8 -*-
import webbrowser


class Movie():
    """
	This class provides a way to store movie related information
	"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
		this is a init function.it defined four features of a movie.
		:param movie_title:
		:param movie_storyline:
		:param poster_image:
		:param trailer_youtube:
		:return Nothing
		"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """this function can open the movie's trailer"""
        webbrowser.open(self.trailer_youtube_url)
