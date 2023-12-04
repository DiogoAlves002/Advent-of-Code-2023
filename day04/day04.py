

def main():
	filename = "input.txt"
	#filename = "test.txt"

	with open(filename, "r") as file:
		inputRead = file.readlines()


	total_part1 = 0

	cardsDict = {}
	for i in range(1, len(inputRead) + 1):
		cardsDict[i] = 1 # initial cards

	for line in inputRead:
		# parsing stuff
		card, game = line.split(": ")

		card_idx = int(card.split(" ")[-1])

		winning_numbers, numbers_we_have = game.replace("\n", "").split(" | ")
		
		winning_numbers_set = set(winning_numbers.split(" "))
		numbers_we_have_set = set(numbers_we_have.split(" "))

		if "" in winning_numbers_set: 
			winning_numbers_set.remove("")

		if "" in numbers_we_have_set: 
			numbers_we_have_set.remove("")

		match_numbers = winning_numbers_set.intersection(numbers_we_have_set)

		# part 1
		points = 0 if not match_numbers else 1 << len(match_numbers) - 1
		total_part1 += points

		# part 2
		for i in range(1, len(match_numbers) + 1):
			cardsDict[card_idx + i] = cardsDict[card_idx + i] + cardsDict[card_idx]
			


	total_part2 = sum(cardsDict.values())

	print("part 1:", total_part1)
	print("part 2:", total_part2)



if __name__ == "__main__":
	main()
