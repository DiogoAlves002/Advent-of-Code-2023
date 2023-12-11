

def main():
	filename = "input.txt"
	#filename = "test.txt"

	with open(filename, "r") as file:
		input_read = file.readlines()

	all_next_values = []
	all_previous_values = []
	for line in input_read:
		seq_str = line.split()
		seq = []
		for num in seq_str:
			seq.append(int(num))

		last_nums = [seq[-1]]
		first_nums = [seq[0]]
		
		while any(n != 0 for n in seq):
			next_seq = []
			for i in range(len(seq) - 1):
				next_seq.append(seq[i + 1] - seq[i])
			seq = next_seq
			last_nums.append(seq[-1])
			first_nums.append(seq[0])

		next_value = sum(last_nums)
		all_next_values.append(next_value)

		# this could have been done in one go if I had gone for recursion but fuck it we ball
		previous_value = 0
		for i in range(len(first_nums) - 2, -1, -1):
			previous_value = first_nums[i] - previous_value
		all_previous_values.append(previous_value)

	
		
	print("Part 1:", sum(all_next_values))
	print("Part 2:", sum(all_previous_values))



if __name__ == "__main__":
	main()
