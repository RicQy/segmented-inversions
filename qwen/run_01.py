# Qwen attempt 1 (placeholder, intentionally incorrect solution).
# Idea: compute total inversions once and divide by k.
# This is NOT correct for this problem but is a plausible naive attempt.

import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        # Coordinate compression
        vals = sorted(set(a))
        comp = {v: i for i, v in enumerate(vals)}
        c = [comp[x] for x in a]

        inv = 0
        for i in range(n):
            for j in range(i + 1, n):
                if c[i] > c[j]:
                    inv += 1

        # Wrong heuristic: spread inversions evenly across k segments
        ans = (inv + k - 1) // k
        print(ans)

if __name__ == "__main__":
    solve()

