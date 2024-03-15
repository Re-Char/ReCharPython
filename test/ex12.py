import time
from sys import argv
from os.path import exists
script, src_name, test_name = argv

print(f"I will copy from {src_name} to {test_name}")
src_target = open(src_name)
src_data = src_target.read()

print(f"The input file is {len(src_data)} bytes long")
print(f"Does the test file exists? {exists(test_name)}")

print("If ready, press 'S' to start")
input()
test_target = open(test_name, 'w')
test_target.write(src_data)
for i in range(3):
    time.sleep(0.5)
    print('.', end='')

test_target = open(test_name)
print("\nThe test file's content is:\n", test_target.read())

print("All things have been done!!!")
src_target.close()
test_target.close()
