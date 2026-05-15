# =========================================
# 🎬 Movie Class
# =========================================

class Movie:

    # Constructor
    def __init__(self, title, genre, rating):

        self.title = title
        self.genre = genre
        self.rating = rating


    # Method
    def show_details(self):

        print("Movie:", self.title)
        print("Genre:", self.genre)
        print("Rating:", self.rating)



# =========================================
# Main Program
# =========================================
# This code runs ONLY if file is executed directly
# =========================================

if __name__ == "__main__":

    movie1 = Movie(
        "Interstellar",
        "Sci-Fi",
        9.0
    )

    movie1.show_details()