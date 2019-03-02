
"""
Tic Tac Toe
"""


def draw_field(field):
    for row in range(5):
        if row % 2 == 0:
            pratical_row = int(row/2)
            for column in range(5):
                if column % 2 == 0:
                    practical_column = int(column/2)
                    if column != 4:
                        print(field[practical_column][pratical_row], end="")
                    else:
                        print(field[practical_column][pratical_row])
                else:
                    print("|", end="")
        else:
            print("-----")


Player = 1
CurrentField = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]
draw_field(CurrentField)
while True:
    print("Players turn: ", Player)
    MoveRow = int(input("please enter the row: "))
    MoveColumn = int(input("please enter the column: "))  # reason for the int is because every input is a string
    if Player == 1:
        #make move for player 1
        if CurrentField[MoveColumn][MoveRow] == " ":
            CurrentField[MoveColumn][MoveRow] = "X"
            Player = 2
    else:
        #make move for player 2
        if CurrentField[MoveColumn][MoveRow] == " ":
            CurrentField[MoveColumn][MoveRow] = "O"
            Player = 1
    draw_field(CurrentField)
