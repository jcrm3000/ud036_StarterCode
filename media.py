#Importing the library "webbrowser" to be able to use the "open" class
import webbrowser



#Creating a parent class

class Video:
    
    #Creating the constructor of the class and puting the attributes to it

    def __init__(self, title, duration):

        #Initializing the attributes variables
        
        self.title = title
        self.duration = duration

#Creating a child class
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


        


