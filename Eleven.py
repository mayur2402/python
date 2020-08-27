'''
	Accept N numbers from user and display all such elements which are
multiples of 11.
Input :N :6
Elements : 85 33 45 67 89 99
Output : 33 99

'''
class Eleven:
	def __init__(self,iArr,iNo):
		self.iArr = iArr
		self.iNo = iNo
	def Display(self):
		for iCnt in range(self.iNo):
			if(self.iArr[iCnt] % 11 == 0):
				print(self.iArr[iCnt])


iNo = int(input("How many numbers"))
iArr = []
if(iNo <= 0):
	print("Error : Invalid Argument")
	exit(-1)

for iCnt in range(iNo):
	ele = int(input("Enter number"))
	iArr.append(ele)

eObj = Eleven(iArr,iNo)
eObj.Display()
