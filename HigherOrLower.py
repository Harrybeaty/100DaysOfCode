# A game where the user guesses which artist has higher or lower sales.
import random
# To Do
# Create album dictionary
albums_dict = {
    "Michael Jackson - Thriller": 72,
    "AC/DC - Back in Black": 52,
    "Eagles - Their Greatest Hits": 48,
    "Whitney Houston - The Bodyguard Soundtrack": 47,
    "Pink Floyd - The Dark side of the Moon": 45,
    "Meatloaf - Bat Out of Hell": 44,
    "Eagles - Hotel California": 43,
    "Shaina Twain - Come On Over": 41,
    "Fleetwood Mac - Rumours": 40,
    "Bee Gees - Saturday Night Fever": 39,
    "Led Zeppelin - Led Zeppelin IV": 38,
    }
# Generate random album.
def choose_album(dict):
    keys_list = list(dict.keys())
    return random.choice(keys_list)

# select 2 albums
score = 0
known_album_name = choose_album(albums_dict)
album_unknown = choose_album(albums_dict)
# Make sure the albums are different.
def albums_different(album1, album2, dict):
    while album1 == album2:
        album2 = choose_album(dict)

    return album2    
# Display albums, sales and ask question.
game_over = False
while not game_over:
    known_album_sales = albums_dict[known_album_name]
    albums_dict.pop(known_album_name)
    album_unknown_sales = albums_dict[album_unknown]
    user_answer = ""
    while user_answer != "higher" or user_answer != "lower":
        user_answer = input(f"Did {album_unknown} have higher or lower sales than {known_album_sales} million sales of {known_album_name}? Higher/Lower ").lower()
        if user_answer == "higher" or user_answer == "lower":
            if album_unknown_sales > known_album_sales and user_answer == "higher" or album_unknown_sales < known_album_sales and user_answer == "lower":
                print("You are correct!!")
                score += 1
                print(f"Your score is {score}.")
                known_album_name = album_unknown
                if score == 10:
                    print("You Win")
                    break
                album_unknown = albums_different(known_album_name, album_unknown, albums_dict)
            else:
                print(f"Incorrect, game over, your score is {score}")
                game_over = True
