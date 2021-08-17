from datetime import datetime

name = input("Give me your name: ")
age = int(input("Give me your age: "))

print(
    f'{name}, you will be 100 years old in {datetime.now().year + 100 - age}.')
