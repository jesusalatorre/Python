def generate_list():
	from random import randint
	rows=int(raw_input("Renglones en la lista: "))
	resultant=[]
	for num in range(rows):
		resultant.append(randint(0,100))
		print resultant[num]
	raw_input("click anything to sort")
	pos=0
	for row in range(0,rows):
		for num in range(pos,rows):
			if resultant[num]<resultant[row]:
				bubble=resultant[row]
				resultant[row]=resultant[num]
				resultant[num]=bubble
		pos=pos+1
	for num in range(rows):
		print resultant[num]
generate_list()
raw_input("Press anything to finish")