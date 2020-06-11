lang = { 'Aniket' : ['c','c++','java','python','swift','c#'],'Devarshi' : ['c','c++','java'] ,'Sagar' : ['c','c++','java']}
print(lang)
print('---------------------------------------------------------------------')
print("Aniket's languages are",lang['Aniket'])
print("Devarshi's languages are",lang['Devarshi'])
print("Sagar's languages are",lang['Sagar'])
print('---------------------------------------------------------------------')
for name,lan in lang.items():
	if len(lan) > 3:
		print(name ,'\t' ,lan)
print('---------------------------------------------------------------------')
for name,lan in lang.items():
	print(name ,'language')
	for l in lan:
		print(l)
print('---------------------------------------------------------------------')

friend = { 'Aniket' : {'c','c++','java','python','swift','c#'},'Devarshi' : {'c','c++','java'} ,'Sagar' : {'c','c++','java'}}
print(friend)
print('---------------------------------------------------------------------')
print("Aniket's languages are",friend['Aniket'])
print("Devarshi's languages are",friend['Devarshi'])
print("Sagar's languages are",friend['Sagar'])
print('---------------------------------------------------------------------')
for name,lan in friend.items():
	if len(lan) > 3:
		print(name ,'\t' ,lan)
print('---------------------------------------------------------------------')
for name,lan in friend.items():
	print(name ,'language')
	for l in lan:
		print(l)
print('---------------------------------------------------------------------')

