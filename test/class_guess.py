from textwrap import dedent
import random


class Play(object):
    def __init__(self):
        print(dedent("""
                     The computer will generate a random number between 1 and 30,
                     you totally have 5 chances to guess it.
                     Now, let's begin!
                     """))
        print('Please input your first guess number:', end='')
        self.guess_num(int(input()))

    def guess_num(self, guess):
        num = random.randint(1, 30)
        count = 1
        while guess != num and count < 5:
            if guess > num:
                print(f"Your guess number is bigger!\nYou only have {5 - count} chances!\n")
            elif guess < num:
                print(f"Your guess number is smaller!\nYou only have {5 - count} chances!\n")
            guess = int(input("Please input your next number:"))
            count += 1
        if guess == num:
            print("Congratulations, you make it!!!")
            self.judge(count)
        else:
            print("Oh no, you failed. The number is:", num)

    def judge(self, count):
        if count == 1:
            print(f"You just use {count} chances, you are a lucky dog!")
        elif 1 < count <= 3:
            print(f"You only use {count} chances, good job!")
        else:
            print(f"Although you totally use {count} chances, you make it.")


play = Play()
