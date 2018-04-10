import webbrowser


#Creating a parent class
class Video:
    #Creating the constructor of the class and puting the attributes to it
    def __init__(self, title, duration):
        #Initializing the attributes variables
        self.title = title
        self.duration = duration


#Creating a child class of the class "Video"
class Movie(Video):

    #Creating the constructor of the class and puting the attributes to it
    def __init__(self, title, duration, storyline, poster_image,
                 trailer_youtube):
        
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Creating a class method to be able to show trailers
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


#Creating a child class of the class "Movie"
#being the grandchild of the class "Video"
class Tv_show(Movie):
    
    #Creating the constructor of the class and puting the attributes to it
    def __init__(self, title, duration, storyline,
                 poster_image, trailer_youtube,
                 seasons, episodes, tv_station):
        
        Movie.__init__(self, title, duration, storyline,
                       poster_image, trailer_youtube)
        self.seasons = seasons
        self.episodes = episodes
        self.tv_station = tv_station


