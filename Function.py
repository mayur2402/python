def fun1():
	"""function without parameter"""
	print("Hello")
fun1()
print('------------------------------------------')

def fun2(name):
	"""function with parameter"""
	print("Hello,",name.title())
fun2('sagar')
print('------------------------------------------')

def fun3(name,lang):
	"""function with two parameter"""
	print(name.title()+"'s favourite language is",lang.title())
fun3('Aniket','java')
fun3('Devarshi','c')
fun3(lang = 'cpp',name = 'sagar')
print('------------------------------------------')

def fun4(name,sport = 'Cricket'):
	"""function with default argument"""
	print(name.title()+"'s favourite sport is",sport.title())
fun4(name = 'Aniket')
fun4('Devarshi','Kho-Kho')
fun4('sagar')
print('------------------------------------------')

def fun5(name1,name2,name3):
	"""function returning value"""
	name = name1.title()+" "+name2.title()+" "+name3.title()
	return name
friend = fun5('sagar','devarshi','aniket')
print(friend)
print('------------------------------------------')

def fun6(lang1,lang2,lang3 = ''):
	"""function for optional argument"""
	return lang1+" "+lang2+" "+lang3
language1 = fun6('c','c++','c#')
language2 = fun6('java','python')
print(language1)
print(language2)
print('------------------------------------------')

def fun7(lang1,lang2,lang3):
	"""function returning dictionary"""
	return {'aniket' : lang1, 'Devarshi' : lang2, 'sagar' : lang3}
language = fun7('c','c++','c#')
print(language)
print('------------------------------------------')

def fun8(langs):
	"""function with parameter as list"""
	for lang in langs:
		print(lang.title())
fun8(['c','c++','c#','java','python','swift','Go'])
print('------------------------------------------')

def fun9(name,*language):
	"""function Arbitrary Number of Arguments"""
	print(name,language)
fun9('sagar','c','c++','c#','java')
fun9('aniket','c','c++','c#','java','python','swift')
fun9('Devarshi','c','c++','java')
print('------------------------------------------')

def fun10(name,lang):
	"""function call by while loop"""
	return name.title()+" "+lang.title()
while True:
	print("Enter 'q' to quit") 
	name = input('Enter name ')
	if name == 'q':
		break
	lang = input('Enter Language ')
	if lang == 'q':
		break
	name_lang = fun10(name,lang)
	print(name_lang)
print('------------------------------------------')
