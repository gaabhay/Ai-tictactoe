plane = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]


values = {
    "X": 1,
    "tie": 0,
    "O": -1
}


def print_board_state(board):



    print("\n#########################\n")
    for row in plane:
        print(row[0], row[1], row[2])
    print("\n#########################\n")


def winner(plane):

    # horizontal win
    for i in range(len(plane)):
        if plane[i][0] == plane[i][1] and plane[i][1] == plane[i][2]:
            if plane[i][0] == "X":
                return "X"
            if plane[i][0] == "O":
                return "O"

    # vertical win
    for i in range(len(plane[0])):
        if plane[0][i] == plane[1][i] and plane[1][i] == plane[2][i]:
            if plane[0][i] == "X":
                return "X"
            if plane[0][i] == "O":
                return "O"

    # diagonal win 1
    if plane[0][0] == plane[1][1] and plane[1][1] == plane[2][2]:
        if plane[0][0] == "X":
            return "X"
        if plane[0][0] == "O":
            return "O"

    # diagonal win 2
    if plane[2][0] == plane[1][1] and plane[1][1] == plane[0][2]:
        if plane[2][0] == "X":
            return "X"
        if plane[2][0] == "O":
            return "O"

    # continue
    for row in plane:
        for cell in row:
            if cell == "-":
                return "continue"

    # tie
    return "tie"


def minimax(plane, is_this_AIs_turn):


    winner_player = winner(plane)

    # if we reached the end of the tree
    if winner_player != "continue":
        return values[winner_player]

    # if this is AIs turn i.e the maximizing players turn
    if is_this_AIs_turn:
        score = - 2  # anything smaller than min score
        for i in range(len(plane)):
            for j in range(len(plane[0])):
                if plane[i][j] == "-":
                    plane[i][j] = "X"
                    curr_score = minimax(plane, False)
                    plane[i][j] = "-"
                    score = max(score, curr_score)
        return score
    else:
        score = 2  # anything bigger than max score
        for i in range(len(plane)):
            for j in range(len(plane[0])):
                if plane[i][j] == "-":
                    plane[i][j] = "O"
                    curr_score = minimax(plane, True)
                    plane[i][j] = "-"
                    score = min(score, curr_score)
        return score


def ais_move(plane):


    score = - 2  # anything smaller than min score
    x = -1  # the row no. of cell which AI chosses for best move
    y = -1  # the column no. of cell which AI chosses for best move

    for i in range(len(plane)):
        for j in range(len(plane[0])):
            if plane[i][j] == "-":
                plane[i][j] = "X"
                curr_score = minimax(plane, False)
                plane[i][j] = "-"
                if curr_score > score:
                    score = curr_score
                    x = i
                    y = j
    return [x, y]


def game(plane):


    will_play = input("Will you play with me? y/N  ")

    if (will_play.upper() == "Y"):

        # printing the initial empty board
        print("")
        print("Initial Empty Board-")
        print_board_state(plane)
        print("")

        # playing the game until it ends
        while winner(plane) == "continue":

            location = input(
                "Enter space seperated row[0-2] and column[0-2] no (0-indexed) of the cell you want to choose: ")
            location = location.strip()
            while True:
                try:
                    space_pos = location.find(" ")
                    x = int(location[: space_pos])
                    y = int(location[space_pos + 1:])

                    # if player makes an illegal move i.e chooses a cell which is already filled
                    if plane[x][y] != "-" or space_pos == -1:
                        location = input(
                            "Please enter valid input for example '1 2'(Note: the entered cell should be empty): ")
                        continue

                    plane[x][y] = "O"
                    break

                # if the player enters wrong or out of bounds cell location
                except:
                    location = input(
                        "Please enter valid input for example '1 2'(Note: the entered cell should be empty): ")
                    location = location.strip()

            print("")
            print("After your Move-")
            print_board_state(plane)
            print("")

            # checking if the game has ended after the player's move
            if winner(plane) == "O":
                print(" YOU WON")
                break

            elif winner(plane) == "X":
                print("I WON")
                break

            elif winner(plane) == "tie":
                print("It's a TIE")
                break

            # AI playing it's move
            AIs_turn = ais_move(plane)
            x = AIs_turn[0]
            y = AIs_turn[1]
            plane[x][y] = "X"

            print("After my Move-")
            print_board_state(plane)
            print("")

            # checking if the game has ended after the AI's move
            if winner(plane) == "O":
                print("YOU WON")
                break

            elif winner(plane) == "X":
                print("I WON")
                break

            elif winner(plane) == "tie":
                print("It's a TIE")
                break


# calling the main function to start the game
game(plane)



