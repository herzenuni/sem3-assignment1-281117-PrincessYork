def digits_pow_sum(number):
	number = str(number)
	sum = 0
	for char in number:
		sum += int(char) ** 2
	return sum

def start():
	print("двузначные :")
	for i in range(10, 100):
		if digits_pow_sum(i) % 17 == 0:
			print(i, end = ', ')
	
	print("\nтрехзначные :")
	for i in range(100, 1000):
		if digits_pow_sum(i) % 17 == 0:
			print(i, end = ', ')
	print()

if __name__ == "__main__":
	start()