x = 2

while x >= 0:
    password = input('Please enter password:')
    if password == 'a123456':
        print('Correct. Welcome.')
        break

    elif password != 'a123456':
        print('Wrong. Please try again.')
        print('You have', x, 'more chances')
        x = x - 1

while x < 0:
	print('You are unauthorised to access this system.')
	raise SystemExit