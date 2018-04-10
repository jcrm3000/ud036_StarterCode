import media
import fresh_tomatoes


#Creating an object of the class "Movie"
toy_story = media.Movie("Toy story",str(2)+" horas",
                        "Toys that are alive",
                        "https://bit.ly/2GKm3Jn",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

#Creating an object of the class "Movie"
avatar = media.Movie("Avatar",str(2)+" horas",
                     "A guy on an alien planet",
                     "https://bit.ly/2Exvhmn",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#Creating an object of the class "Movie"
interstellar = media.Movie("Interstellar",str(2)+" horas",
                           "A guy, who goes into the space",
                           "https://bit.ly/2JzknjN",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

#Creating an object of the class "Tv_show"
breaking_bad = media.Tv_show("Breaking bad",str(100)+" horas",
                              "A professor, how makes drogs",
                              "https://bit.ly/2mC5DE8",
                              "https://www.youtube.com/watch?v=rJnjxvgvkBM",
                               5,62,"RTL")

#Creating an object of the class "Tv_show"
game_of_thrones = media.Tv_show("Game of thrones",str(100)+" horas",
                                "People fighting for the iron throne",
                                "https://bit.ly/2qfYvlq",
                                "https://www.youtube.com/watch?v=v5gsVRxzzI4",
                                8,60,"HBO")

#Creating an array to store all the objects
movies = [toy_story, avatar, interstellar, breaking_bad, game_of_thrones]

#Calling the method "open_movies_page() of the class fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
