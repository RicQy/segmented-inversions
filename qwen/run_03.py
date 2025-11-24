# Qwen attempt 3 (placeholder, intentionally incorrect).
# Idea: use total inversions // k as a guess based on average, which is wrong.

import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        def total_inversions():
            inv = 0
            for i in range(n):
                for j in range(i + 1, n):
                    if a[i] > a[j]:
                        inv += 1
            return inv

        tot = total_inversions()
        print(tot // k)

if __name__ == "__main__":
    solve()

