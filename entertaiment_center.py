import media
import fresh_tomatoes

#Creating an object of the class "Movie"
toy_story = media.Movie("Toy story",str(2)+" horas",
                           "Toys that are alive",
                           "goo.gl/2aVBEy","goo.gl/kS9eph")

#Creating an object of the class "Movie"
avatar = media.Movie("Avatar",str(2)+" horas",
                        "A guy on an alien planet",
                        "goo.gl/89dzc8","goo.gl/gwsavy")

#Creating an object of the class "Movie"
interstellar = media.Movie("Interstellar",str(2)+" horas",
                              "A guy, who goes into the space",
                              "goo.gl/zUuZ2x","goo.gl/wUW7zT")

#Creating an object of the class "Tv_show"
breaking_bad = media.Movie("Breaking bad",str(100)+" horas",
                              "A professor, how makes drogs",
                              "goo.gl/7ZdQT1","goo.gl/CFhcgP",
                               5,62,"RTL")

#Creating an object of the class "Tv_show"
game_of_thrones = media.Movie("Game of thrones",str(100)+" horas",
                              "People fighting for the iron throne",
                              "goo.gl/j7zoqm","goo.gl/KWcbn4",
                               8,60,"HBO")

movies = [toy_story, avatar, interstellar, breaking_bad, game_of_thrones]

fresh_tomatoes.open_movies_page(movies)
