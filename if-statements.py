"""
if conditiono:
    Action

click = False

like = 0

click = True

if click is True:  <-- simpler |or you can do "if click == True:"
    like = like + 1
    click = False

print(like)


"""

Morning = "day light"
Night = "Its night out"
Current = "day light"


if Current == "day light" and Morning is "day light":
    print(True)
else:
    print(Night)

# either or work

if Current is "day light":
    print(True)
elif Morning is Current:
    print(True)
else:
    print(Night)

print("it is", Current)



""" 
Temperature = 20
Therm = 15

print(Therm)

if Temperature < 15:
    Therm = Therm + 5

print(Therm)

Time = "Day"
Sleepy = False
Pajamas = "Off"
In_bed = True

if Time == "Night":
    Pajamas = "On"
elif Time == "Morning":
    Pajamas = 'On'
else:
    Pajamas = "Off"

print(Pajamas)
"""