from enum import Enum


class Directions(Enum):
	NORTH = (-1, 0)
	SOUTH = (1, 0)
	WEST = (0, -1)
	EAST = (0, 1)



def main():
	filename = "input.txt"
	#filename = "test_2.txt"
	#filename = "test_1.txt"

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

	opposite_direction = {
		Directions.NORTH : Directions.SOUTH,
		Directions.SOUTH : Directions.NORTH,
		Directions.EAST : Directions.WEST,
		Directions.WEST : Directions.EAST
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

	#printGrid(grid)
	#print("\nstart:", starting_pos)

	biggest_step = 0
	

	# follow path until it leads back to start
	possible_paths = getPipesNeighboursOfStart(starting_pos, pipe_connections, grid)

	# NOTE maybe go one step in each path at a time
	#      but beware that doing that would follow the correct path twice
	for pipe_and_direction in possible_paths:
		step = 0
		path = set()
		path.add(starting_pos)
		

		pipe_pos, next_direction = pipe_and_direction

		while True:
			step += 1
			path.add(pipe_pos)

			pipe_pos = getNextPipe(pipe_pos, next_direction)
			if pipe_pos == starting_pos:
				biggest_step = int(len(path) / 2)
				break
			if is_point(pipe_pos, grid):
				break
			next_direction = getNextDirection(pipe_pos, next_direction, opposite_direction, pipe_connections, grid)
		
		if biggest_step != 0:
			break

	print("part1:", biggest_step)



def getNextPipe(curr, direction):
	return (curr[0] + direction.value[0], curr[1] + direction.value[1])

def is_point(pipe_pos, grid):
	y, x = pipe_pos

	pipe = grid[y][x]

	return pipe == "."


def getNextDirection(pos, direction, opposite_direction, pipe_connections, grid):
	y, x = pos
	pipe = grid[y][x]

	pipe_directions = pipe_connections[pipe][:]
	direction_we_came_from = opposite_direction[direction]
	pipe_directions.remove(direction_we_came_from)

	next_direction = pipe_directions[0]

	return next_direction


def getNeighbourNextDirection(candidate, pipe_connections):
	if candidate == ".":
		return None

	candidate_directions = pipe_connections[candidate][:]

	if Directions.SOUTH in candidate_directions:
		candidate_directions.remove(Directions.SOUTH)
		next_direction = candidate_directions[0]
		return next_direction

	return None



def getPipesNeighboursOfStart(pos, pipe_connections, grid):
	y, x = pos
	grid_last_y, grid_last_x = len(grid) - 1, len(grid[0]) - 1

	neighbours = [] # neigbour = ( (y, x), direction_we_must_follow_to_reach_it )

	if y > 0:
		candidate = grid[y - 1][x] # up
		
		next_direction = getNeighbourNextDirection(candidate, pipe_connections)

		if next_direction != None:
			neighbours.append(((y - 1, x), next_direction))


	if y < grid_last_y:
		candidate = grid[y + 1][x] # down

		next_direction = getNeighbourNextDirection(candidate, pipe_connections)

		if next_direction != None:
			neighbours.append(((y + 1, x), next_direction))


	if x > 0:
		candidate = grid[y][x - 1] # left

		next_direction = getNeighbourNextDirection(candidate, pipe_connections)

		if next_direction != None:
			neighbours.append(((y, x - 1), next_direction))


	if x < grid_last_x:
		candidate = grid[y][x + 1] # right

		next_direction = getNeighbourNextDirection(candidate, pipe_connections)

		if next_direction != None:
			neighbours.append(((y, x + 1), next_direction))

	return neighbours



def printGrid(grid):
	for row in grid.keys():
		for col in grid[row].keys():
			print(grid[row][col], end="")
		print("")

		




if __name__ == "__main__":
	main()
