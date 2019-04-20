import random
l=['1','2','3','4','5','6','7','8','9']
def printfun():
	print(str(l[0]) + " | " + str(l[1]) + " | " + str(l[2]))
	print("---------")
	print(str(l[3]) + " | " + str(l[4]) + " | " + str(l[5]))
	print("---------")
	print(str(l[6]) + " | " + str(l[7]) + " | " + str(l[8]))
def validator():
	return (l[0]==l[1]==l[2]=='X')or(l[0]==l[3]==l[6]=='X')or(l[0]==l[4]==l[8]=='X')or(l[1]==l[4]==l[7]=='X')or(l[2]==l[5]==l[8]=='X')or(l[2]==l[4]==l[6]=='X')or(l[3]==l[4]==l[5]=='X')or(l[6]==l[7]==l[8]=='X')
def validator1():
	return (l[0]==l[1]==l[2]=='O')or(l[0]==l[3]==l[6]=='O')or(l[0]==l[4]==l[8]=='O')or(l[1]==l[4]==l[7]=='O')or(l[2]==l[5]==l[8]=='O')or(l[2]==l[4]==l[6]=='O')or(l[3]==l[4]==l[5]=='O')or(l[6]==l[7]==l[8]=='O')
def main():
	c=0
	printfun()
	li=[]
	while True:
		inp=input("Enter number within range 1-9 :")
		if inp not in l :
			print("Please enter another input")
			continue
		if inp in li:
			print("Already used position")
			continue
		else:
			li.append(inp)
			ind=l.index(inp)
			l[ind]='X'
			c=c+1
			num=random.randint(1,9)
			while True:
				if (num!=inp)and(str(num) not in li):
					break
				else:
					num=random.randint(1,9)
			l[l.index(str(num))]='O'
			c=c+1
			li.append(str(num))
		if c==6:
			break
		printfun()
	if(validator()):
		print("Congrats")
		printfun()
	else:
		if(validator1()):
			print("Computer won!!!!!")
		else:
			print("Tie")
		printfun()
		print("Do u want to continue dude?? Y|N")
		yes=input()
		if yes=='Y':
			main()


main()
