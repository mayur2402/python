class Perfect:
	def __init__(self,iNo):
		self.iNo = iNo

	def ChkPerfect(self):
		if(self.iNo < 0):
			self.iNo = -self.iNo

		if(self.iNo == 1 or self.iNo == 0):
			return False

		iAdd = 1
		iCnt = 0

		for iCnt in range(2,self.iNo):

			if(self.iNo % iCnt == 0):
				iAdd = iAdd + iCnt

			if(iAdd > self.iNo):
				break

		if(iAdd == self.iNo):
			return True
		else:
			return False

iNo = int(input("\nEnter Number\t:"))

Pobj = Perfect(iNo)
 
bIsPerfect = Pobj.ChkPerfect()

if (bIsPerfect):
	print("Number ",iNo," is perfect number")
else:
	print("Number ",iNo," is not perfect number")
