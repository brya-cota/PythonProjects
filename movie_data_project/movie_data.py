'''
Brya Cota
4/22/26
This program will read data from a CSV file and display it in a formatted table.
'''
import csv

# Prompt the user to enter the name of the CSV file to read.
users_file = input("Welcome to movie data - please enter the name of the CSV file to read: ")

try:
    # Opening file based on user input
    with open(users_file, "r") as file:
        reader = csv.reader(file)

        # Empty dictionary to group movies together from movies.csv
        movies = {}

        # Parse each line and extract the showtime, movie title, and movie rating
        for row in reader:
            showtime = row[0]
            movie_title = row[1]
            rating = row[2]

            # Adding data from movies.csv into empty dict movies{}, group together each movie, with corresponding
            # rating and showtime
            if movie_title not in movies:
                movies[movie_title] = {
                    "rating": rating,
                    # Creating empty list to store the multiple showtimes from each movie_title
                    "showtimes": []
                }
            # Adding the showtime that correlates to the movie title
            movie_data = movies[movie_title]
            show_time = movie_data["showtimes"]
            show_time.append(showtime)

    #Printing header and formatting output header
    print(f'\n{"Movie Title":<44} | {"Rating":>5} | Showtimes')
    print("-" * 99)

    # Printing the actual results
    for movie_title in movies:
        movie_rating = movies[movie_title]["rating"]
        movie_showtimes = movies[movie_title]["showtimes"]

        # All showtimes for the movie are displayed on the same line, separated by a single space.
        times = " ".join(movie_showtimes)

        # Movie Title: Left-justified in a field of a minimum of 44 characters.
        # Rating: Right-justified in a field of 5 characters.
        print(f"{movie_title:<44} | {movie_rating:>5} | {times}")

# Handle any exceptions
except FileNotFoundError:
    print(f"Error: File '{users_file}' not found! Please try again.")
