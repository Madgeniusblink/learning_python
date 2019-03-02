
""""
# Var = input("Message to user")

# Name = input("Please enter your name: ")
# print(Name)
#
# Age = int(input("Please enter your age: "))
# print(Age+1.8)

Scores = []

for score in range(5):
    currentScore = float(input("Please enter score #" + str(score + 1) + ": "))
    Scores.append(currentScore)
    print("Score you entered was:", currentScore, "The score #"+str(score + 1))

print(Scores)
"""

"""
File = open("Filename", "r")  # r, w, a -> append, r+ -> read and write
File.close()


VacationSpots = ["London", "Paris", "NewYork", "Utah", "Iceland"]

VacationFile = open("VacationPlaces", "w")

for Spots in VacationSpots:
    VacationFile.write(Spots + "\n")

VacationFile.close()

VacationFile = open("VacationPlaces", "r")

# TheWholeFile = VacationFile.read()
#
# print(TheWholeFile)

FirstLine = VacationFile.readline()
print(FirstLine)
for line in VacationFile:
    print(line, end="")

VacationFile.close()

FinalSpot = "Thailand"

VacationFile = open("VacationPlaces", "a")
VacationFile.write(FinalSpot)
VacationFile.close()

VacationFile = open("VacationPlaces", "r")
for line in VacationFile:
    print(line, end="")

VacationFile.close()

for time in range(5):
    with open("VacationPlaces"+str(time), "r") as VacationFile:
        for line in VacationFile:
            print(line)

VacationFile.read()


"""



