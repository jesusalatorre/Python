
def multiplication(integer_list):
	result=1
	for num in integer_list:
		result=result*num
	print result

integers=[]
answer=1

while answer!=0:
	answer=int(raw_input("Agrega numeros a la lista, incluye 0 para cerrar lista:"))
	if answer==0:
		break
	integers.append((answer))

multiplication(integers)
raw_input("Teclee para continuar...")





