aliens = { 'green' : 5, 'red' : 10,'black' : 15}
print('green')
print('red')
print('black')
print('--------------------------------------------------------')
print(aliens['green'])
print(aliens['red'])
print(aliens['black'])
print('--------------------------------------------------------')
point = aliens['red']
print('you have earn '+str(point)+' points')
print('--------------------------------------------------------')
alien_0 = {'green' : 5}
alien_0['x_co-ordinate'] = 0
alien_0['y_co-ordinate'] = 25
print(alien_0)
print('--------------------------------------------------------')
alien_1 = {}
alien_1['red'] = 10
alien_1['x_co-ordinate'] = 10
alien_1['y_co-ordinate'] = 30
print(alien_1)
print('--------------------------------------------------------')
alien_2 = {'black' : 15,'x_co-ordinate' : 30,'y_co-ordinate' : 50}
print(alien_2)
alien_2['x_co-ordinate'] = 25
print(alien_2)
print('--------------------------------------------------------')
alien_2['speed'] = 'medium'
print(alien_2)
if alien_2['speed'] == 'slow':
	x_increament = 1
elif alien_2['speed'] == 'medium':
	x_increament = 2
else:
	x_increament = 3

alien_2['x_co-ordinate'] = alien_2['x_co-ordinate'] + x_increament
print(alien_2)	
print('--------------------------------------------------------')
print(aliens)
del aliens['black']
print(aliens)
print('--------------------------------------------------------')

for color,point in aliens.items():	print(color,point)
print(aliens.items())

for color in aliens.keys():
#for color in aliens:
	print(color)
print(aliens.keys())

for point in aliens.values():
	print(point)
print(aliens.values())

print('--------------------------------------------------------')

aliens['yellow'] = 20
print(aliens)
for color,point in sorted(aliens.items()):
	print(color , '\t' , point)

print('--------------------------------------------------------')

alien = []
for no in range(10):
	alienno = {'color' : 'black','point' : 15,'x_co-ordinate' : 30,'y_co-ordinate' : 50}
	alien.append(alienno)
	alienno = {'color' : 'red', 'point' : 20,'x_co-ordinate' : 40,'y_co-ordinate' : 20}
	alien.append(alienno)
	alienno = {'color' : 'orange','point' : 30,'x_co-ordinate' : 20,'y_co-ordinate' : 10}
	alien.append(alienno)

for al in alien:
	print(al)

print(len(alien))
print('--------------------------------------------------------')

for al in alien[0:3]:
	if al['color'] == 'black':
		al['color'] = 'green'
		al['point'] = 50
	print(al)




