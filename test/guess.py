import random
random = random.randint(1, 100)
print('The computer has generated a random number from 1 to 100.')
print('You only have 5 chances.')
guess = int(input("Now, let's start. Please input your first guess number: "))
count = 1
while guess != random and count < 5:
    if guess == random:
        break
    elif guess < random:
        print('Your guess is smaller!!!')
        guess = int(input())
        count += 1
    elif guess > random:
        print('Your guess is bigger!!!')
        guess = int(input())
        count += 1
if guess == random:
    print('The random number is %d.' % random)
    if count == 1:
        print('Congratulations! You only use one chance!')
    elif 1 < count < 5:
        print('You make it!!!')
    else:
        print('Ehh...')
else:
    print('You have ran out of your chances. How stupid you are!!!')