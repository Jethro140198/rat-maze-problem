maze = [[1,0,0,0],
        [1,1,0,1],
        [0,1,0,0],
        [1,1,1,1]]

# Function to print the maze
def print_maze(ma):
    for i in range(len(ma)):
        for j in range(len(ma[0])):
            if j == 3:
                print(str(ma[i][j]))
            else:
                print(str(ma[i][j]) + " ", end = " ")


# Check if the next down and next right is a dead end
def check_valid(row, column, ma):
    if row < len(ma)-1 and column < len(ma[0])-1:
        if ma[row+1][column] == 0 and ma[row][column+1] == 0:
            return False

    if row == 3 and column < len(ma[0])-1:
        if ma[row][column+1] == 0:
            return False

    if row < 3 and column == len(ma[0])-1:
        if ma[row+1][column] == 0:
            return False

    return True


# Check if the mouse is able to move to the next available space
def check_around(row, column, ma):
    if row > 0 and column > 0:
        if ma[row-1][column] != 7 and ma[row][column-1] != 7:
            return False
    if row == len(ma)-1 and column == 0:
        if ma[row-1][column] != 7:
            return False
    if row == len(ma)-1 and column > 0:
        if ma[row-1][column] != 7 and ma[row][column-1] != 7:
            return False

    return True


# Function to solve the maze
def solve_maze(ma):
    for i in range(len(ma)):
        for j in range(len(ma[0])):
            if ma[i][j] == 1:
                if check_around(i,j,ma):
                    if check_valid(i,j,ma):
                        ma[i][j] = 7
                        solve_maze(ma)
    return


print_maze(maze)
print("\n")
solve_maze(maze)
print_maze(maze)
