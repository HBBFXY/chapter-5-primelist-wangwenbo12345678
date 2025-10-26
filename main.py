def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def PrimeList(N):
    primes = []
    for num in range(2, N):
        if is_prime(num):
            primes.append(str(num))
    return ' '.join(primes)
if __name__ == "__main__":
    print(PrimeList(10)) 
