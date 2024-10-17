# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Finding all prime numbers between 1 and 250
prime_numbers = [num for num in range(1, 251) if is_prime(num)]

# Writing the prime numbers to a file
with open('results.txt', 'w') as file:
    for prime in prime_numbers:
        file.write(f"{prime}\n")

print("Prime numbers between 1 and 250 have been written to results.txt")
