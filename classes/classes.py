# class className:

#     def __init__(self):
#         self.Attribute = 0

#     def AnotherFunction(self):


class Team:
    def __init__(self, name = "Name", location = "Location", language = "English"):
        self.TeamName = name
        self.TeamLocation = location
        self.TeamLanguage = language
        self.TeamInfo = name, location, language
    
    def name(self, name):
        self.TeamName = name
    
    def location(self, location):
        self.TeamLocation = location
    
    def language(self, language):
        self.TeamLanguage = language

    



Team1 = Team("colombia Int", "Colombia", "ENGLISH")
Team2 = Team("Russia Int", "Russua, MO", "RUSSIA")
Team3 = Team("USA Int", "LA, US", "INT")


print(Team1.TeamName, Team1.TeamLocation)

print(f"the team name is {Team1.TeamName} and the team location is {Team1.TeamLocation}")

print(Team1.TeamInfo)

