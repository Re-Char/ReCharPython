from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi, {user_name}! Welcome to the ex10 script.")
print("Now, let's begin!")

print("Please input your age:")
input(prompt)
print("Please input your gender:")
input(prompt)
print("Please input your nationality:")
input(prompt)

print("""
Ok, you make it!
Congratulations!
Thank you for your participating!
""")
