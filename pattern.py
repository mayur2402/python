'''
	accept input from user and display below pattern

	input	:	4	4

	output	:	*  *  *  #	1,1  1,2  1,3  1,4		2  3  4  5
			*  *  #  *	2,1  2,2  2,3  2,4		3  4  5  6
			*  #  *  *	3,1  3,2  3,3  3,4		4  5  6  7
			#  *  *  *	4,1  4,2  4,3  4,4		5  6  7  8
'''
class Pattern:
	def __init__(self,Row,Col):
		self.Row = Row
		self.Col = Col

	def Display_Pattern(self):
		for i in range(self.Row):
			for j in range(self.Col):
				if(i+j != self.Col-1):
					print("*\t",end = "")
				else:
					print("#\t",end = "")
			print("\n")


iRow = int(input("\nHow many rows\t"))
iCol = int(input("\nHow many columns\t"))

if(iRow != iCol or iRow == 0 or iCol ==0):
	print("Error : Invalid Argument")
else:
	Pobj = Pattern(iRow,iCol)
	Pobj.Display_Pattern()


