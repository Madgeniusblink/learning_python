
# # Fav Artist #
# Artist = "Drake"
# # Type of music #
# Genre = "Hip hop music"
# # Title #
# Song_Title = "In My Feelings"
# # Duration #
# Duration_In_Seconds = 450
# # Emotion Classification #
# Spectrum_Emotion = "Happy"
# # how easy it is to dance to it #
# Dance_Ability = "High"
# # is it an energetic song? yes #
# Energy = "High"
# # high volume? yes #
# Loudness = "high"
#
# print(Artist)
# print(Genre)
# print(Song_Title)
# print(Duration_In_Seconds)
# print(Spectrum_Emotion)
# print(Dance_Ability)
# print(Energy)
# print(Loudness)
import posixpath

# Key : Value

# for key, value in FavoriteSongs.__iter__():
#     print(key, value)

# for key in FavoriteSongsDescription:
#     print(key, ":", FavoriteSongsDescription[key])


# def guess_value():
#     while True:
#         try:
#             print("This are the characteristics of my favorite song.\n My Favorite Song is 'In My Feelings'")
#             for key, val in FavSongDetail.items():
#                 guess = input("Can you guess the characteristic of one of my Fav Song Detail? \n{}: ".format(key))
#             if FavSongDetail[key] != FavSongDetail[val]:
#                 print("Sorry That is not the right {}".format(val))
#         except KeyError:
#             print("Sorry that is the wrong answer")
#             print(guess)

# 7
FavSongDetail = {"Artist": "drake",  # how to create a set inside a Dictionary?
                 "Genre": "Hip Hop",
                 "Song Title": "In My Feelings",
                 "Duration In Seconds": "450",
                 "Spectrum Emotion": "Happy",
                 "Dance Ability": "High",
                 "Energy": "High",
                 "Loudness": "High"}


def guess_value():
    try:
        print("can you guess the characteristics of my favorite song?\n My Favorite Song is 'In My Feelings'")
        for key, val in FavSongDetail.items():
            guess = input("{}: ".format(key)).lower()
            if guess == val in FavSongDetail.values():
                print(True)
            elif guess != val:
                print(False, "Sorry! Try again in the next round")
                continue
    finally:
        print(FavSongDetail)

    # restart all over if 3 or more are wrong(False) then restart
    # if guess.False is 3 >=:  # for range(3, False) in guess_value():
    #   restart the loop(action)
    # else:
    #   print("Congrats you pass")


guess_value()

