
def main():
    filename = "input.txt"
    #filename = "test.txt"

    with open(filename, "r") as file:
        input = file.readlines()


    all_numbers = []
    all_gear_ratios = []

    for row, line in enumerate(input):

        col = 0
        while col < len(line):

            # part 1
            number = ""
            is_valid = False
            while col < len(line) and line[col].isnumeric():
                number += line[col]
                
                if is_valid == False and hasSymbolAround(row, col, input):
                    is_valid = True
                col += 1

            if is_valid:
                all_numbers.append(int(number))

            
            # part 2
            if line[col] == "*":
                numbers_around = getNumbersAround(row, col, input)
                if len(numbers_around) == 2:
                    gear_ratio = numbers_around[0] * numbers_around[1]
                    all_gear_ratios.append(gear_ratio)

            col += 1


            




    print("part 1: ", sum(all_numbers))
    print("part 2: ", sum(all_gear_ratios))



def isOutOfBounds(row, col, input):
    return (col < 0 or row >= len(input) or row < 0 or col >= len(input[0]))


def hasSymbolAround(row, col, input):
    y = -1

    for _ in range(3):
        x = -1
        for __ in range(3):
            if isOutOfBounds(row + y, col + y, input):
                x += 1
                continue

            candidate = input[row + y][col + x]
            if candidate != "." and not candidate.isnumeric() and candidate != "\n":
                return True
            
            x += 1
        y += 1

    return False

def getNumbersAround(row, col, input):
    all_numbers = []

    y = -1

    for _ in range(3):
        x = -1
        numbers_in_line = set()
        for __ in range(3):
            if isOutOfBounds(row + y, col + x, input):
                x += 1
                continue

            if input[row + y][col + x].isnumeric():
                numbers_in_line.add(getNumber(input[row + y], col + x))

            x += 1

        all_numbers += list(numbers_in_line)
        y += 1

    return all_numbers



def getNumber(line, col):
    number = line[col]

    starting_point = col
    while col + 1 < len(line) - 1 and line[col + 1].isnumeric():
        number += line[col + 1]
        col += 1

    col = starting_point
    while col - 1 > - 1 and line[col - 1].isnumeric():
        number = line[col-1] + number
        col -= 1


    return int(number)








if __name__ == "__main__":
    main()

