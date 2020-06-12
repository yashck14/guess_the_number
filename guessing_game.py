from random import randrange as r
a = int(input("number :- "))
b = int(input("number :- "))
chance = {}
for i in range(1,3):
	c = r(a,b)
	chance["player{0}".format(i)] = 0
	u = 0
	while u != c:
		u = int(input("your guess"))
		if u in range(a,b):
			if u == c:
				print("you win\n")
				if i == 1:
					print(f"\nnow player{i} chance\n")
			else:
				print("try again")
				chance["player{0}".format(i)] = chance["player{0}".format(i)] + 1
		else:
			print("your digit is not in range")
			

if int(chance['player1']) > int(chance['player2']):
	print("player 1 lose")
else:
	print("player 2 lose")
