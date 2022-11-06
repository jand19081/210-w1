# Assignment:
#    cse210 week1: Tic-Tac-Toe
# Author:
#    Jarom Anderson

# Initialize board.
def initialize_board():
    """Creates a dictionary of an empty tic-tac-toe table"""
    board = {"row1": [1, 2, 3], "row2": [4, 5, 6], "row3": [7, 8, 9]}
    return board

# Draw board
def draw_board(board):
    # Print line 1
    line = board["row1"]
    print(f"{line[0]} | {line[1]} | {line[2]}")
    print("-+-+-") 
    # Print line 2
    line = board["row2"]
    print(f"{line[0]} | {line[1]} | {line[2]}")
    print("-+-+-")
    # Print line 3
    line = board["row3"]
    print(f"{line[0]} | {line[1]} | {line[2]}")
    print() 

# Change board
def play(board, player):
    """Asks user to choose a square.
        Returns: New board data
    """
    played = False

    while played == False:
        # Ask user for to pick a square
        choice = int(input(f"{player}'s turn to choose a square (1-9): "))

        if choice < 4:
            board["row1"][choice - 1] = player
            played = True
        elif choice > 3 and choice < 7:
            board["row2"][choice - 4] = player
            played = True
        elif choice > 6:
            board["row3"][choice - 7] = player
            played = True
        else:
            print("Sorry that's not a valid choice.")

    return board

# small function to check line for a win
def check_line(line):
    if line[0] == "x" and line[1] == "x" and line[2] == "x":
        return True
    elif line[0] == "o" and line[1] == "o" and line[2] == "o":
        return True
    else:
        return False


# Check for win
def check_board(board):
    "Checks board for three in a row"
    
    # Check row 1:
    line = board["row1"]
    win = check_line(line)
    if win == True:
        player = line[1]
        return [win, player]
    
    # Check row 2
    line = board["row2"]
    win = check_line(line)
    if win == True:
        player = line[1]
        return [win, player]

    # Check row 3
    line = board["row3"]
    win = check_line(line)
    if win == True:
        player = line[1]
        return [win, player]

    # Check Column 1
    line = [board["row1"][0], board["row2"][0], board["row3"][0]]
    win = check_line(line)
    if win == True:
        player = line[1]
        return [win, player]

    # Check Column 2
    line = [board["row1"][1], board["row2"][1], board["row3"][1]]
    win = check_line(line)
    if win == True:
        player = line[1]
        return [win, player]

    # Check Column 3
    line = [board["row1"][2], board["row2"][2], board["row3"][2]]
    win = check_line(line)
    if win == True:
        player = line[1]
        return [win, player]

    # Check diagonal top-left to bottom-right
    line = [board["row1"][0], board["row2"][1], board["row3"][2]]
    win = check_line(line)
    if win == True:
        player = line[1]
        return [win, player]

    # Check diagonal top-right to bottom-left
    line = [board["row1"][2], board["row2"][1], board["row3"][0]]
    win = check_line(line)
    if win == True:
        player = line[1]
        return [win, player]

    # Check if board is full
    line = board["row1"] + board["row2"]+ board["row3"]
    count = 0
    for element in line:
        if type(element) == str:
            count += 1

    if count == 9:
        return count

def check_win(board):
    # If there's a win, returns list [win, player]
    # If the board is full, returns a 9
    result = check_board(board)

    if type(result) == list:
        print()
        draw_board(board)
        print(f"{result[1]} wins. Good game.")
        quit()
    elif type(result) == int:
        print()
        draw_board(board)
        print("No one wins. Better luck next time.")
        quit()



def main():

    # Initialize board
    board = initialize_board()
    # Set first player as 'x'
    player = "x"
    
    start = False

    print("Welcome to the Tic-Tac-Toe game!")
    print("-" * 30)

    # Ask user if they are ready
    while start == False:
        ready = input("Enter 1 to start: ")
        if int(ready) == 1:
            start = True
        else:
            print("Sorry you entered an invalid value.")
            print("Try again")
            print()
            print()
    
    while start == True:
        print()
        # Draw board
        draw_board(board)
        # Change board
        board = play(board, player)
        # Check for a win
        check_win(board)
         
        # Change player
        if player == "x":
            player = "o"
        else:
            player = "x"


if __name__ == "__main__":
    main()