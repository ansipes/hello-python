word = input("Enter a word: ")

m = [x for i, x in enumerate(word[:len(word)//2]) if word[i] != word[-i - 1]]

if len(m) == 0:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")
