import threading
import os
import time

class Test:
	def test1(self):
		T = threading.currentThread()
		print("Name = ",T.getName())

		for i in range(1,11):
			print(T.getName(),"\t",i)
			time.sleep(1)

if __name__ == "__main__" :
	T = threading.current_thread()

	print("Name = ",T.getName())

	obj1 = Test()

	T1 = threading.Thread(target = obj1.test1)
	T2 = threading.Thread(target = obj1.test1)

	T1.start()
	T2.start()

