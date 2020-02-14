#pattern4
for i in range(1,6):
	for j in range(1,6):
		if i==1 or i==5:
			print("* ",end="")
		elif j==1 or j==5:
			print("* ",end="")
		elif i+j==6:
			print("$ ",end="")
		else :
			print("  ",end="")
	print("")

