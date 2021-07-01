def main():
  list = [7, 8, 9]
  ford = {
    "year": 1999,
    "make": "Ford",
    "model": "Some Shit"
  }
  for item in ford:
    print(f'{item}: {ford[item]}')

if __name__ == "__main__": main()