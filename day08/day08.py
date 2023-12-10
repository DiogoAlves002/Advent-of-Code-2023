from math import lcm

def main():
	filename = "input.txt"
	#filename = "test_1.txt"
	#filename = "test_2.txt"
	#filename = "test_part2.txt"
	#filename = "test_part2_2.txt"

	with open(filename, "r") as file:
		inputRead = file.readlines()

	instructions = inputRead[0].replace("\n", "")
	instructions_len = len(instructions)

	node_network = {}
	starting_nodes = [] # part 2

	for line in inputRead[2:]:
		node, following_nodes = line.split(" = ")
		following_nodes = following_nodes[1:-2].split(", ")
		node_network[node] = {
			"L": following_nodes[0], 
			"R": following_nodes[1]
			}
		if node[-1] == "A":
			starting_nodes.append(node)



	# part 1
	# NOTE: the test inputs given were made for their specific challenge, so this block of code will not work for any test_part2.txt
	i, step_part_1 = 0, 0
	current_node = "AAA"
	while current_node != "ZZZ":
		current_node = node_network[current_node][instructions[i]]

		i = (i + 1) % instructions_len
		step_part_1 += 1


	# part 2
	# NOTE: this algorithm is too slow
	""" i_2, step_2 = 0, 0
	while any(node[-1] != "Z" for node in starting_nodes):
		next_nodes = []
		for node in starting_nodes:
			next_direction_int = getNextDirection(instructions, i_2)
			next_node = node_network[node][next_direction_int]

			next_nodes.append(next_node)

		starting_nodes = next_nodes
		i_2 = (i_2 + 1) % instructions_len
		step_2 += 1 """

	# part 2 
	
	# figuring out the cycles

	starting_nodes_cycle = {} 
	# ex:
	# a -> c -> e -> z -> b -> e
	# 0    1    2    3    4    5
	# 0    1   e1+0 e1+1 e1+2 e2+0

	# a: (path to cycle - a-c), (cycle - e z b - start = 1, length = 3, z_step = [1, ])

	for node in starting_nodes:
		starting_node = node

		visited = {} # visited[node] = (i = 1, i = 3, ...)
		z_steps = [] # steps at which a Z node was visited
		
		step_2 = 0
		instruction_i = 0

		while node not in visited or instruction_i not in visited[node][0]:
			if  node not in visited :
				visited[node] = [(instruction_i, step_2)]
			else:
				visited[node].append((instruction_i, step_2))

			if node[-1] == "Z":
				z_steps.append(step_2)
				

			node = node_network[node][instructions[instruction_i]]

			instruction_i = (instruction_i + 1) % instructions_len
			step_2 += 1

		# found beggining of cycle
		for visit in visited[node]:
			if visit[0] == instruction_i:
				first_visit_step = visit[1]

		# NOTE: this ended up being overkill since all paths in input only cross z one time and its within the loop
		before_loop = ()
		after_loop = ()
		for z_step in z_steps:
			if z_step < first_visit_step: # before loop
				before_loop += (z_step, )
			else: # during loop
				after_loop += (z_step - first_visit_step, )
		ordered_z_steps = [before_loop, after_loop]




		starting_nodes_cycle[starting_node] = (first_visit_step, step_2 - instruction_i, ordered_z_steps) # (start, length, z_steps)

	# this should work faster than the previous attempt but its still pretty slow so im not gonna test it
	""" i = 0
	while True:
		z_in_loop = set()
		for node in starting_nodes:
			loop_start, length, z_steps = starting_nodes_cycle[node]
			z_step = z_steps[1][0]
			next_z = loop_start - 1 + z_step + length * i
			z_in_loop.add(next_z)

		if len(z_in_loop) == 1: # they were all in the same step :D
			step_part_2 = z_in_loop.pop()
			break

		i+=1 """

	# im not enterily sure why this gives the correct answer (shouldnt we have take into account the start of the loop ???)
	step_part_2 = lcm(*[i[1] for i in starting_nodes_cycle.values()])

	print("part 1:", step_part_1)
	print("part 2:", step_part_2)
		 
	


if __name__ == "__main__":
	main()
