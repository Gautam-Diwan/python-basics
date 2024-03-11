primes = [2, 3, 5, 7]

for prime in primes:
    print(prime)

print("Incrementing")
count = 0
while count < 5:
    print(count)
    count += 1

print('Decrementing')
while True:
    if count < 0:
        break

    print(count)
    count -= 1

print("print even numbers")
for i in range(20):
    if i % 2:
        continue
    print(i)