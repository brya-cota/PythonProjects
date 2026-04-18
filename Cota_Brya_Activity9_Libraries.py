'''
Brya Cota
CSC101
4/8/26
This program will select several random artists to listen to from a given playlist
'''

# Importing random module
import random

playlist = ["Bad Bunny", "Drake", "The Weeknd", "Doja Cat", "Sabrina Carpenter", "Don Toliver"]

# Shuffle playlist
(random.shuffle(playlist))
print(f"Shuffled Playlist: {playlist}")

# Choosing random artist to listen to
print(f"Random Choice from Playlist: {random.choice(playlist)}")

#Skip to random position in the list of artists
chose_artist = int(input("Which artist would you like to listen to? "
                         "\nChoose: \n1 for Bad Bunny \n2 for Drake \n3 for The Weeknd \n"
                         "4 for Doja Cat \n5 for Sabrina Carpenter \n6 for Don Toliver\n"))

random_artist = random.randint(0, 6)
print(f"Sorry they're not available, you get {playlist[random_artist]} instead.")

# Choosing a random artist based on the length of the playlist
print(f"Random Artist from Playlist (Based on the numbers above): {random.randrange(len(playlist))}")