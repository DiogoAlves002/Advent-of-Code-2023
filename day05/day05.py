
class ToMap:
	def __init__(self, destination):
		self.destination = destination
		self.ranges = []

	def addRange(self, new_range_list):
		new_range = tuple([int(n) for n in new_range_list]) 

		assert(len(new_range) == 3)

		self.ranges.append(new_range)

	def convertValue(self, value):
		destination_value = value # default is same as value

		for convertion_range in self.ranges:
			destination_range_start, source_range_start, range_len = convertion_range
			range_len -= 1

			# if within range
			if value >= source_range_start and value <= source_range_start + range_len:

				# convert value
				convertion_value = destination_range_start - source_range_start
				destination_value = value + convertion_value
				break

		return destination_value

	

	def getDestination(self):
		return self.destination


	

def getSeedLocationValue(seed_value, maps):
	source = "seed"

	while source != "location":
		curr_map = maps[source]
		seed_value = curr_map.convertValue(seed_value)
		source = curr_map.getDestination()

	return seed_value




def main():
	filename = "input.txt"
	#filename = "test.txt"

	# parsing stuff
	with open(filename, "r") as file:
		inputRead = file.readlines()

	seeds = inputRead[0].replace("seeds: ", "").replace("\n", "").split(" ")
	seeds = [int(n) for n in seeds]
	maps = {} # curr = ToMap(curr)
	
	for line in inputRead[1: ]:
		if line == "\n":
			continue

		tokens = line.replace("\n", "").split(" ")

		if tokens[-1] == "map:":
			curr_map = tokens[0]
			curr_to, to, follow = curr_map.split("-")
			maps[curr_to] = ToMap(follow)
			continue

		maps[curr_to].addRange(tokens)


	# computing locations for part 1
	location_values_part1 = []
	for seed_value in seeds:
		location_value = getSeedLocationValue(seed_value, maps)
		
		location_values_part1.append(location_value)



	# computing locations for part 2
	location_values_part2 = []
	for i in range(0, len(seeds), 2):
		range_start = seeds[i]
		range_len = range_start + seeds[i + 1]

		for seed_value in range(range_start, range_len):
			location_value = getSeedLocationValue(seed_value, maps)
			location_values_part2.append(location_value)






	print("part 1:", min(location_values_part1))
	print("part 2:", min(location_values_part2))
	



if __name__ == "__main__":
	main()
