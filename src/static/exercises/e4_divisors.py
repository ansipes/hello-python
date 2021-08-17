num = int(input("Enter a number: "))
divisors = [x for x in range(1, num // 2 + 1) if num % x == 0]
divisors.append(num)

print(divisors)
