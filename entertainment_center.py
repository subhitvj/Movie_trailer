"""Stores details of movies and displays them on a website."""
import media
import fresh_tomatoes


def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
        poster image link, video trailer link and release date."""

    gully_boy = media.Movie("Gully Boy",
                            "Gully Boy is a film about a 22 YO boy from India",
                            "https://upload.wikimedia.org/wikipedia/en/0/07/Gully_Boy_poster.jpg",
                            "https://www.youtube.com/watch?v=JfbxcD6biOk",
                            "14 Feb 2019")
    uri = media.Movie("URI",
                      "IA who did surgical strike against militants in POK",
                      "https://upload.wikimedia.org/wikipedia/en/3/3b/URI_-_New_poster.jpg",
                      "https://www.youtube.com/watch?v=VVY3do673Zc",
                      "11 Jeb 2019")
    rampage = media.Movie("Rampage",
                          "A story of a man who shares an bond with animal",
                          "https://upload.wikimedia.org/wikipedia/en/6/6b/Rampage_teaser_film_poster.jpg",
                          "https://www.youtube.com/watch?v=coOKvrsmQiI",
                          "03 April 2018")
    the_pursuit = media.Movie("The Pursuit of Happyness",
                              "Life of father, doing best for his son",
                              "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                              "https://www.youtube.com/watch?v=89Kq8SDyvfg",
                              "05 Dec 2006")
    ek_ladki = media.Movie("Ek Ladki Ko Dekha To Aisa Laga",
                           "A young woman and her life problems",
                           "https://upload.wikimedia.org/wikipedia/en/4/4f/Ek_Ladki_Ko_Dekha_Toh_Aisa_Laga_poster.jpg",
                           "https://www.youtube.com/watch?v=pKcamCgBvMo",
                           "01 Feb 2019")
    total_dhamaal = media.Movie("Total Dhamaal",
                                "Bunch of peoples, doing treasure hunt",
                                "https://upload.wikimedia.org/wikipedia/en/e/e7/Total_Dhamaal_poster.jpg",
                                "https://www.youtube.com/watch?v=fo9EhcwQXcM",
                                "22 Feb 2019")

    movies = [the_pursuit, gully_boy, uri, rampage, ek_ladki, total_dhamaal]
# Store the Movie objects in a list.
    fresh_tomatoes.open_movies_page(movies)
# Open the movie website in the user's browser, featuring the movies above.

if __name__ == '__main__':
    main()
