



#creating a class called Movie
class Movie:

    #creating the constructor of the class and puting the properties to it
    
    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):

        #initializing the properties variables
        
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
