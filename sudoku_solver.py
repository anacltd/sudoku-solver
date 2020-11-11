def line_to_grid(line: str) -> list:
    sub_line = [line[i:i + 9] for i in range(0, len(line), 9)]
    return [[int(i) for i in l] for l in sub_line]


def pprint_grid(grid):
    print("- " * 13)
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- "*13)
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            elif j == 0:
                print("| ", end="")
            print(grid[i][j], end="") if j == 8 else print(str(grid[i][j]) + " ", end="")
        print(" |")
    print("- " * 13)


def solve(grid):
    found = find_empty(grid)
    if not found:
        return True
    else:
        row, column = found

    for i in range(1, 10):
        if is_valid(grid, i, (row, column)):
            grid[row][column] = i
            if solve(grid):
                return True
            grid[row][column] = 0
    return False


def is_valid(grid, number, position):
    # check row
    for i in range(len(grid[0])):
        if grid[position[0]][i] == number and position[1] != i:
            return False

    # check column
    for i in range(len(grid)):
        if grid[i][position[1]] == number and position[0] != i:
            return False

    # check square
    box_x, box_y = position[1] // 3, position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == number and (i, j) != position:
                return False
    return True


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return None


if __name__ == '__main__':
    line = input("Enter your sudoku grid as a single line with 0 instead of empty boxes\n")
    if len(line) == 81:
        grid = line_to_grid(line)
        print("\nSolving...\nDone!\n")
        solve(grid)
        pprint_grid(grid)
    else:
        print(f"Error: you entered {len(line)} numbers instead of 81!")
