seasons = ['game of thrones','vikings','money heist','stranger things','dark','witcher','chernobyl','walking dead','lost in space']
if 'breaking bad' in seasons:
	print('good')
else:
	for season in seasons:
		print(season.title())
print('----------------------------------------------------------')
if 'scared games' not in seasons:
	print('must watch sacred games')
print('----------------------------------------------------------')
for season in seasons:
	if season == 'money heist':
		print(season+ ' in spanish/english language')
	elif season == 'dark':
		print(season+ 'in german/english language')
	else:
		print(season+ ' in english/hindi language')
print('----------------------------------------------------------')
for season in seasons:
	if season == 'money heist':
		print('sorry '+season+ ' is not in hindi language')
	elif season == 'dark':
		print('sorry '+season+ ' is not in hindi language')
	else:
		print(season+ ' is in hindi language')
print('----------------------------------------------------------')

seasons1 = []
if seasons1:
	for season1 in seasons1:
		print(season1+' is favourite indian season')
else:
	print('you have not seen any indian season')
print('----------------------------------------------------------')

request_season = ['game of thrones','breaking bad','sacred game','witcher','mirzapur']
for request in request_season:
	if request in seasons:
		print(request+' is available to watch')
	else:
		print(request+' is not available to watch')
print('----------------------------------------------------------')

