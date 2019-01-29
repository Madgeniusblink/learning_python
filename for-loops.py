"""
Length = 50
ToPrint = "-"
for pos in range(1, Length+1):
    print(ToPrint*pos)

for pos in range(Length-1, 0, -1):
    print(ToPrint*pos)

"""

""" 
for row in range(5):
    if row % 2 == 0:
        for column in range(1,6):
            if column % 2 == 1:
                if column != 5:
                    print(" ", end="")
                else:
                    print(" ")
            else:
                print("|", end="")
    else:
        print("------")
"""

# def drawing_board(row, column):
#     for rows in range(5):
#         if rows % 2 == 0:
#             print(" | | ")
#         else:
#             print("------")
#
# drawing_board()


def draw(rows, coloumns):
    for x in range(0, rows):
        if (x % 2 == 0):
            for y in range(1, coloumns + 1):
                if (y % 2 == 1):
                    if (y != coloumns):
                        print(" ", end='')
                    else:
                        print(" ")

                else:
                    print("|", end='')
        else:
            print("------")

draw(5,5)
