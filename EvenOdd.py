class Difference:
	def __init__(self,iArr,iNo):
		self.iArr = iArr
		self.iNo = iNo
		self.iAns = 0
	def Display(self):
		for iCnt in range(iNo):
			if self.iArr[iCnt] % 2 == 0:
				self.iAns += iArr[iCnt]
			else:
				self.iAns -= iArr[iCnt]
		return self.iAns

iArr = []
iNo = int(input("How many numbers"))
print("Enter numbers");
for iCnt in range(iNo):
	ele = int(input())
	iArr.append(ele)
dObj = Difference(iArr,iNo)
iDiff = dObj.Display()
print("Differnce between even elements and odd elements are ",iDiff)
