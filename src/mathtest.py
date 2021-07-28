# add
def add(x, y):
  return x + y

# subtract
def subtract(x, y):
  return x - y

# multiply
def multiply(x, y):
  return x * y

# divide
def divide(x, y):
  return x / y

def main():
  print(f'1 + 2 = {add(1, 2)}')
  print(f'3 - 4 = {subtract(3, 4)}')
  print(f'5 * 6 = {multiply(5, 6)}')
  print(f'7 / 8 = {divide(7, 8)}')

if __name__ == "__main__": main()