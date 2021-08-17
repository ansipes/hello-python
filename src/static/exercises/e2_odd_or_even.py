n = int(input("Give me a numerator: "))
d = int(input("Give me a denominator: "))

if n % d == 0:
    print(f"{n} is divisible by {d}")
else:
    print(f"{n} is not divisible by {d}")

print(f'{n} {("is not", "is")[n % d == 0]} divisible by {d}')
