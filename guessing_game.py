# yash kushwaha
# all errors are handled
from random import randrange as r
while True:
	try:
		a = int(input("enter first number :- \n"))
		b = int(input("enter second number :- \n"))
		break
	except:
		continue 
chance = {}
print("\nplayer1 chance\n")
for i in range(1,3):
	c = r(a,b)
	chance["player{0}".format(i)] = 0
	u = 0
	while u != c:
		while True:
			try:
				u = int(input("your guess "))
				break
			except:
				continue	
		if u in range(a,b):
			if u == c:
				print("you win\n")
				if i == 1:
					print(f"---------------\nnow player2 chance\n")
			else:
				print("try again\n")
				chance["player{0}".format(i)] = chance["player{0}".format(i)] + 1
		else:
			print("your digit is not in range\n")
			
if int(chance['player1']) > int(chance['player2']):
	print("player 1 lose \nplayer 2 win")
elif int(chance['player1']) == int(chance['player2']):
	print("draw")
else:
	print("player 2 lose\nplayer 1 win")
