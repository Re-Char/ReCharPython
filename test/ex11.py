import time
from sys import argv
script, filename = argv

txt = open(filename)
print("There is your file's content:\n", txt.read())

print("I'm going to clear your file content...")
for i in range(3):
    time.sleep(0.5)
    print('.', end='')
print("\nOk, I have done!!!")
txt = open(filename, 'w')

print("\nNow I will make you input 3 lines:")
line1 = input("Please input 1st line:")
line2 = input("Please input 2nd line:")
line3 = input("Please input 3rd line:")
print("Mow I will write these lines to your txt.")
txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line2)
txt.write("\n")

txt = open(filename, 'r')
print("There is your new file's content:\n", txt.read())
txt.close()
