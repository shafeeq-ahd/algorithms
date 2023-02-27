def pisano_period(m):
    current, next = 0, 1
    period = 0
    while True:
        current, next = next, (current + next) % m
        period += 1
        if current == 0 and next == 1:
            return period


def fib_mod(n, m):
    current, next = 0, 1
    for _ in range(n):
        current, next = next, (current + next) % m

    return current


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fib_mod(n % pisano_period(m), m))
