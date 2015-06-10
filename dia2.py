def line():
	print("#==========#")



line()
for i in range(1,5):
	print("|"+(4-i)*" " + "<" +(i*2)*"." + ">" + (4-i)*" "+"|")
for j in range(4,0,-1):
	print("|"+(4-j)*" " + "<" +(j*2)*"." + ">" + (4-j)*" "+"|") 
line()