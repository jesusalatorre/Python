#printdatetime
from datetime import datetime
answer=raw_input("Would you like to know the current date and time? y/n \n")
if (answer=="y"or answer=="Y"):
	print "The current date and time is: \n" + datetime.now()
else:
	print "Closing..."