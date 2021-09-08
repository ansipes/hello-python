def isPrime(n):
  divisors = [x for x in range(1, n // 2 + 1) if n % x == 0]
  divisors.append(n)

  return len(divisors) == 2

n = int(input("Enter a number: "))

if isPrime(n):
  print("This number is prime.")
else:
  print("This number is not prime.")