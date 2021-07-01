def main():
  ford = {
    "year": 1999,
    "make": "Ford",
    "model": "Some Shit"
  }
  for key in ford:
    print(f'{key}: {ford[key]}')

if __name__ == "__main__": main()