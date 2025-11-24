import random

def gen_one(n_max=10, val_max=10):
    n = random.randint(1, n_max)
    k = random.randint(1, n)
    a = [random.randint(1, val_max) for _ in range(n)]
    return n, k, a

def main():
    T = 5
    print(T)
    for _ in range(T):
        n, k, a = gen_one()
        print(n, k)
        print(*a)

if __name__ == "__main__":
    main()

