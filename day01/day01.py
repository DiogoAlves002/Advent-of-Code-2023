
def main():
	filename = "input.txt"
	total_1, total_2 = 0, 0

	numbers = {
		"one" : "1", 
		"two" : "2", 
		"three" : "3", 
		"four" : "4", 
		"five" : "5", 
		"six" : "6", 
		"seven" : "7", 
		"eight" : "8", 
		"nine" : "9"
		}


	with open(filename, "r") as file:
		for line in file:
			l, r = getCalibrationValueDigitsIdx(line) 
			total_1 += int(line[l] + line[r])
	
			total_2 += getCalibrationValuesDigitsAndNames(line, numbers)


	print(total_1)
	print(total_2)
						

def getCalibrationValueDigitsIdx(line):
	l, r = 0, len(line) - 1
	while l < len(line) - 1 and not line[l].isdigit():
		l += 1
	while r > 0 and not line[r].isdigit():
		r -= 1

	return (l, r)

def containsDigits(line):
	return any((char.isdigit() for char in line))
	
def rindex(lst, value):
    i = lst[::-1].index(value[::-1])
    return len(lst) - i - 1



def getCalibrationValuesDigitsAndNames(line, numbers):
	first = ("", len(line)) # (number, idx)
	last = ("", -1) # (number, idx)

	for n in numbers.keys():
		if n in line:
			idx_l = line.index(n)
			idx_r = rindex(line, n)
			if idx_l < first[1]:
				first = (numbers[n], idx_l)
			if idx_r > last[1]:
				last = (numbers[n], idx_r)


	if containsDigits(line):
		l, r = getCalibrationValueDigitsIdx(line)

		if l < first[1]:
			first = (line[l], l)
		if r > last[1]:
			last = (line[r], r)

	return (int(first[0] + last[0]))

		


if __name__ == "__main__":
	main()
