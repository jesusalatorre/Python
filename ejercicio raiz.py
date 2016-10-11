
def find_roots(A,B,C):
	from math import sqrt
	D=B**2-4*A*C
	if A==0:
		print "Linea recta"
		X= (-1)*C/B
		str(X)
		print "X= %s" % X
	elif D==0:
		print "Reales e iguales"
		X_1=((-1)*B)/(2*A)
		X_2=X_1
		str(X_1)
		str(X_2)
		print "X_1= %s" % X_1
		print "X_2= %s" % X_2
	elif D>0:
		print "Reales y distintas"
		DD=sqrt(D)
		X_1=((-1)*B+DD)/(2*A)
		X_2=((-1)*B-DD)/(2*A)
		str(X_1)
		str(X_2)
		print "X_1= %s" % X_1
		print "X_2= %s" % X_2
	elif D<0:
		print "Complejas"
		D=(-1)*D
		CC=sqrt(D)
		imaginary=CC/(2+A)
		X_1=(-1)*B/(2*A)
		X_2=(-1)*B/(2*A)
		str(X_1)
		str(X_2)
		str(CC)
		print "Raiz 1= %s + %si" %(X_1, imaginary)
		print "Raiz 2= %s - %si" %(X_2, imaginary)

A=int(raw_input("A: "))
B=int(raw_input("B: "))
C=int(raw_input("C: "))
find_roots(A,B,C)
raw_input("Teclea para salir")