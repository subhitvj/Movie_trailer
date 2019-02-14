import webbrowser


class Movie():
    """This class provides a way to store movie related information.
    Attributes:
        title: represents title of the movie.
        storyline: gives plot idea of the movie.
        poster_image_url: represents movie poster.
        trailer_youtube_url: movie trailer.
        movie_release_date: represents release date of the movie.
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_date):
        """Initialises class instance."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_release_date = release_date

    def show_trailer(self):
        """function plays the movie trailer in the web browser."""
        webbrowser.open(self.trailer_youtube_url)
