"""

"""

# Participant_Number = 5
# Participant_Data = []
# registered_participants = 0
# outputfile = open("ParticipantData.txt", "w")
#
# while registered_participants <= Participant_Number:
#     TemPartData = []  # name, country, age
#     name = input("What is your name? : ")
#     TemPartData.append(name)
#     country = input("Please enter your country of origin: ")
#     TemPartData.append(country)
#     age = int(input("What is your age #?: "))
#     TemPartData.append(age)
#     Participant_Data.append(TemPartData)
#     print(Participant_Data)
#
#     registered_participants += 1
#
# for participant in Participant_Data:
#     for data in participant:
#         outputfile.write(str(data))  # str(25) -> "25"
#         outputfile.write(" ")
#     outputfile.write("\n")
#
#
# outputfile.close()

inputFile = open("ParticipantData.txt", "r")

input_list = []

for line in inputFile:
    tempParticipant = line.strip("\n").split()
    # print(tempParticipant)
    input_list.append(tempParticipant)
    # print(input_list)
    # "Max US 21 ".strip("\n") - > "Max US 21 "
    # "Max US 21 ".split() -> ["max", "US", "21",]

Age = {}
print(input_list)
for part in input_list:
    tempAge = int(part[-1])
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1

print(Age)

Country = {}

for part in input_list:
    tempCountry = part[1]
    if tempCountry in Country:
        Country[tempCountry] += 1
    else:
        Country[tempCountry] = 1
print("Countries that attended:", Country)
Oldest = 0
Youngest = 100
MostOccuringAge = 0
counter = 0

for tempAge in Age:
    if tempAge > Oldest:
        Oldest = tempAge
    if tempAge < Youngest:
        Youngest = tempAge
    if Age[tempAge] >= counter:
        counter = Age[tempAge]
        MostOccuringAge = tempAge

print(Oldest)
print(Youngest)
print("most occuring age is:", MostOccuringAge, "With", counter, "participants")
inputFile.close()
