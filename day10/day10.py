from enum import Enum


class Directions(Enum):
	NORTH = (1, 0)
	SOUTH = (-1, 0)
	WEST = (0, -1)
	EAST = (0, 1)



def main():
	filename = "input.txt"
	filename = "test_2.txt"
	filename = "test_1.txt"

	STARTING_CHAR_TYPE = "S"
	grid = {} # {col_y : {row_x: char}}


	pipe_connections = {
		"|" : [Directions.NORTH, Directions.SOUTH],
		"-" : [Directions.EAST, Directions.WEST],
		"L" : [Directions.NORTH, Directions.EAST],
		"J" : [Directions.NORTH, Directions.WEST],
		"7" : [Directions.SOUTH, Directions.WEST],
		"F" : [Directions.SOUTH, Directions.EAST],
	}
	

	with open(filename, "r") as file:
		input_read = file.readlines()


	for row, line in enumerate(input_read):
		new_row = {}
		for col, pipe in enumerate(line[:-1]):
			new_row[col] = pipe
			if pipe == STARTING_CHAR_TYPE:
				starting_pos = (row, col)
		grid[row] = new_row

	printGrid(grid)
	print("\nstart:", starting_pos)

	# TODO follow path until it leads back to start

	possible_paths = getPipesNeighboursOfStart(starting_pos, pipe_connections, grid)

	# NOTE maybe go one step in each path at a time
	#      but beware that doing that would follow the correct path twice
	for pipe_and_direction in possible_paths:
		visited = set()
		visited.add(starting_pos)

		pipe, next_direction = pipe_and_direction

		while pipe != starting_pos and pipe not in visited:
			visited.add(pipe)
			pipe = getPosFromDirection(pipe, next_direction)
			# TODO update  next_direction



def getPosFromDirection(curr, direction):
	return (curr[0] + direction.value[0], curr[1] + direction.value[1])





def getNextPipe(pos, direction_from, grid):
	pass




def getPipesNeighboursOfStart(pos, pipe_connections, grid):
	y, x = pos
	grid_last_y, grid_last_x = len(grid) - 1, len(grid[0]) - 1

	neighbours = [] # neigbour = ( (y, x), direction_we_must_follow_to_reach_it )

	if y > 0:
		candidate = grid[y - 1][x] # up

		candidate_directions = pipe_connections[candidate]

		if Directions.SOUTH in candidate_directions:
			candidate_directions.remove(Directions.SOUTH)
			next_direction = candidate_directions[0]

			neighbours.append(((y - 1, x), next_direction))


	if y < grid_last_y:
		candidate = grid[y + 1][x] # down

		candidate_directions = pipe_connections[candidate]

		if Directions.NORTH in candidate_directions:
			candidate_directions.remove(Directions.NORTH)
			next_direction = candidate_directions[0]

			neighbours.append(((y + 1, x), next_direction))


	if x > 0:
		candidate = grid[y][x - 1] # left

		candidate_directions = pipe_connections[candidate]

		if Directions.WEST in candidate_directions:
			candidate_directions.remove(Directions.WEST)
			next_direction = candidate_directions[0]

			neighbours.append(((y, x - 1), next_direction))

	if x < grid_last_x:
		candidate = grid[y][x + 1] # right

		candidate_directions = pipe_connections[candidate]

		if Directions.EAST in candidate_directions:
			candidate_directions.remove(Directions.EAST)
			next_direction = candidate_directions[0]
			
			neighbours.append(((y, x + 1), next_direction))

	return neighbours



def printGrid(grid):
	for row in grid.keys():
		for col in grid[row].keys():
			print(grid[row][col], end="")
		print("")

		




if __name__ == "__main__":
	main()
