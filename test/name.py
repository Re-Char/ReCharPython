name = input()
surname = ''
firstname = ''
point = 0
for x in name:
    if x != ' ':
        if point == 0:
            surname += x
        if point == 1:
            firstname += x
    else:
        point = 1
print('Your surname is: %s' % surname)
print('Your first name is: %s' % firstname)
print('Your full name is: %s' % name)
