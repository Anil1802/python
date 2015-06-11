def box(w,h):
	print (w*"*")
	for i in range(h-2):
		print("*"+(w-2)*" "+"*")
	print(w*"*")

box(10,5)