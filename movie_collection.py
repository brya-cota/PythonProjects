'''
Brya Cota
2/26/26
This program will create a number of lists to manage a movie collection and customer purchase system.
I'll be practicing accessing elements, slicing, modifying lists, and using built-in list methods.
'''

movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump",
          "Inception", "The Matrix", "Goodfellas", "The Lord of the Rings", "Fight Club"]
genres = ["Drama", "Crime", "Action", "Crime", "Drama", "Sci-Fi", "Sci-Fi", "Crime", "Fantasy", "Drama"]
movie_price = [12.99, 14.99, 13.99, 11.99, 10.99, 15.99, 12.99, 13.99, 16.99, 11.99]

#***Accessing and Slicing Lists***
# Using list operations access and display the following information:

# Access the second movie title and its genre and price.
print(f"Second Movie:\nTitle: {movies[1]}\nGenre: {genres[1]}\nPrice: ${movie_price[1]}\n")

# Access the last movie using negative indexing.
print(f"Last Movie:\nTitle: {movies[-1]}\n")


# Display the first 3 movie titles.
print(f"First 3 Movie Titles:\n{movies[:3]}\n")

# Display the last 2 genres.
print(f"Last 2 Genres:\n{genres[-2:]}\n")

# Create a new list sci_fi_movies from movie_titles that includes only the 6th and 7th movies using slicing.
print(f"Sci-Fi Movies:\n{movies[5:7]}\n")

# Create a list top_prices from movie_prices that includes every other price (using slicing with step).
top_prices = movie_price[::2]
print(f"Top Prices:\n{top_prices}")

#***Modify Lists***
# Modify existing lists to simulate changes in the movie store inventory:

# Replace the third movie title in movie_titles with "Interstellar".
# Replace its genre with "Sci-Fi" and update its price to 13.49. Print updated list.
del movies[2]
movies.insert(2, "Interstellar")
print(f"\nAfter Replacing 3rd Movie:\n{movies}")
del genres[2]
genres.insert(2, "Sci-Fi")
print(genres)
del movie_price[2]
movie_price.insert(2, 13.49)
print(movie_price)

# Append a new movie "Black Panther" to movie_titles. Append its genre "Action" and price 10.99 to the respective lists.
# Print updated list.
movies.append("Black Panther")
print(f"\nAfter Appending New Movie:\n{movies}")
genres.append("Action")
movie_price.append(10.99)
print(genres)
print(movie_price)

# Insert a movie "Up" at index 2 with genre "Animation" and price 7.99. Print updated list.
movies.insert(2, "Up")
genres.insert(2, "Animation")
movie_price.insert(2, 7.99)
print(f"\nAfter inserting 'Up' at index 2:\n{movies}")
print(genres)
print(movie_price)

#***Removing and Measuring Data***
# Use remove() to delete "Black Panther" from movie_titles, and also remove its corresponding genre and price by index.
movies.remove("Black Panther")
del genres[11]
del movie_price[11]

# Use pop() to remove the last movie from the movie_titles list and store it in a variable named removed_movie.
# Also pop the corresponding genre and price.
removed_movie = movies.pop()
removed_genre = genres.pop()
removed_movie_price = movie_price.pop()

# Print the removed movie.
print(f"\nRemoved Movie: {removed_movie}\n")

# Print the length of each list (movie_titles, movie_genres, movie_prices) using len().
print(f"List Lengths:\nMovies: {len(movies)}")
print(f"Genres: {len(genres)}")
print(f"Movies Price: {len(movie_price)}")
