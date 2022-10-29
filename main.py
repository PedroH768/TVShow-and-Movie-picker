import pandas as pd
import random


movies = pd.read_csv('movies_final.csv', sep=';', index_col=0)
shows = pd.read_csv('shows_final.csv', sep=';', index_col=0)


movie_list = movies.values
show_list = shows.values


def show_movies():
    mov = random.randint(0, len(movie_list))
    print("Movie: " + movie_list[mov][0])
    print("Release date: " + str(movie_list[mov][2]))
    print("Duration: " + str(movie_list[mov][4]))
    print("IMDB Score: " + str(movie_list[mov][7]))
    print("Genre(s): " + str(movie_list[mov][5]))
    print("Country: " + str(movie_list[mov][6]))
    print("Description: " + str(movie_list[mov][1]))
    print("Available on: " + str(movie_list[mov][9]))

def show_shows():
    sh = random.randint(0, len(show_list))
    print("TV Show: " + show_list[sh][0])
    print("Release date: " + str(show_list[sh][2]))
    print("Seasons: " + str(show_list[sh][6]))
    print("IMDB Score: " + str(show_list[sh][7]))
    print("Genre(s): " + str(show_list[sh][4]))
    print("Country: " + str(show_list[sh][5]))
    print("Description: " + str(show_list[sh][1]))
    print("Available on: " + str(show_list[sh][9]))


print("Would you like to watch a movie(1) or a TV Show(2) ?")

ans = input()

while ans != "1" and ans != "2":
    print("ERROR : Invalid answer")
    ans = input()

print('')
print('')

if ans == "1":
    show_movies()
elif ans == "2":
    show_shows()
