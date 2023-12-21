
def main():
	filename = "input.txt"
	filename = "test_2.txt"
	filename = "test_1.txt"

	STARTING_CHAR_TYPE = "S"
	grid = {} # {col_y : {row_x: char}}
	

	with open(filename, "r") as file:
		input_read = file.readlines()


	for row, line in enumerate(input_read):
		new_row = {}
		for col, character in enumerate(line[:-1]):
			new_row[col] = character
			if character == STARTING_CHAR_TYPE:
				starting_pos = (row, col)
		grid[row] = new_row

	printGrid(grid)
	print("\nstart:", starting_pos)

	# TODO breadth first or something to find where the path leads back to start
	# NOTE record (y, x) in visited to know the distance later

	

def printGrid(grid):
	for row in grid.keys():
		for col in grid[row].keys():
			print(grid[row][col], end="")
		print("")

		




if __name__ == "__main__":
	main()
