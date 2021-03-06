from task2 import digits_pow_sum

def test_1():
	lst = list()
	for i in range(10, 100):
		if digits_pow_sum(i) % 17 == 0:
			lst.append(i)
	assert(lst == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92])

def test_2():
	lst = list()
	for i in range(100, 1000):
		if digits_pow_sum(i) % 17 == 0:
			lst.append(i)
	assert(lst == [104, 117, 140, 155, 171, 208, 209, 223, 232, 277, 280, 290, 305, 322, 334, 343, 350, 401, 410, 433, 446, 464, 503, 515, 530, 551, 588, 589, 598, 599, 607, 644, 668, 669, 670, 686, 696, 706, 711, 727, 760, 772, 802, 820, 858, 859, 866, 885, 895, 902, 920, 958, 959, 966, 985, 995])