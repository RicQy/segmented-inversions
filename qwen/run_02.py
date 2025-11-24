# Qwen attempt 2 (placeholder, intentionally incorrect).
# Idea: always cut segments of roughly equal length, ignoring inversions.

import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        # Partition positions into k nearly equal segments
        base = n // k
        extra = n % k

        segments = []
        i = 0
        for seg in range(k):
            size = base + (1 if seg < extra else 0)
            j = i + size
            segments.append((i, j))
            i = j

        def inv_on_segment(l, r):
            cnt = 0
            for i in range(l, r):
                for j in range(i + 1, r):
                    if a[i] > a[j]:
                        cnt += 1
            return cnt

        best = 0
        for l, r in segments:
            best = max(best, inv_on_segment(l, r))

        print(best)

if __name__ == "__main__":
    solve()

