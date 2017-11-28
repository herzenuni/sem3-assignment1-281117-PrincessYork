def digits_sum(number):
	number = str(number)
	sum = 0
	for char in number:
		sum += int(char)
	return sum

def start():
	number = int(input("number = "))
	print("Sum of digits in {} = {}".format(number, sum_of_digits(number)))

if __name__ == "__main__":
	start()