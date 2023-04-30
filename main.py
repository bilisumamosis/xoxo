# modeling of the game
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]

# by default player X starts the game
currentPlayer = "X"

noPlays = 0

# empty XO
print(f"   1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")



def singlePlay(currentPlayer, noPlays):
    # getting where current player wants to play
    userPos = input(f"Player {currentPlayer} :")
    x = int(userPos[0]) - 1
    y = int(userPos[1]) - 1


    # insuring that the play is valid
    while(

        # checking if its not a floating point
        int(userPos) != float(userPos) or
        # checking it's in range
        int(userPos) < 11 or
        int(userPos) > 33
    ):
        userPos = input(f"Player {currentPlayer} please input a valid index:")
        x = int(userPos[0]) - 1
        y = int(userPos[1]) - 1
    while(
            # checking if its empty
            map[x][y] != " "

    ):
        userPos = input(f"Player {currentPlayer} please input a free place:")
        x = int(userPos[0]) - 1
        y = int(userPos[1]) - 1

    noPlays = noPlays + 1

    map[x][y] = currentPlayer
    print(f"   1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")


def win(map):
    combs = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 0)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)]
    ]

    for i in range(len(combs)):
        if map[combs[i][0][0]][combs[i][0][1]] != " " and map[combs[i][1][0]][combs[i][1][1]] != " " and map[combs[i][2][0]][combs[i][2][1]]:
            if map[combs[i][0][0]][combs[i][0][1]] == map[combs[i][1][0]][combs[i][1][1]] and map[combs[i][0][0]][combs[i][0][1]] == map[combs[i][2][0]][combs[i][2][1]] and map[combs[i][1][0]][combs[i][1][1]] == map[combs[i][2][0]][combs[i][2][1]]:
                return True

    return False


while (noPlays <= 9 and win(map) == False):

    singlePlay(currentPlayer, noPlays)
    if (win(map)):
        print(f"GAME OVER\n Player {currentPlayer} wins!")
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


