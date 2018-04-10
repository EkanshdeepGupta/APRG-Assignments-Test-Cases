from random import *

f = open("/home/ekansh/Programming/Python/Assignments/TestCases2/test_2_9.py", "w")

'''x = []

for a in range(1000000):
	x.append(randint(-100, 100))

f.write("x" + " = " + str(x))

f.close()'''

x = []

for a in range(1000000):
	m = randint(1, 10**15)
	n = randint(1, min(10**15-m, 10**6))

	x.append((m, m+n))

f.write("x" + " = " + str(x))

f.close()



