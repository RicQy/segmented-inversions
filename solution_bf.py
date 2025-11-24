import sys
from functools import lru_cache

def min_max_inv_bruteforce(a, k):
    n = len(a)

    @lru_cache(None)
    def inv(l, r):
        # inversion count on subarray [l, r] (0-based, inclusive)
        cnt = 0
        for i in range(l, r):
            for j in range(i + 1, r + 1):
                if a[i] > a[j]:
                    cnt += 1
        return cnt

    best = 10**18

    def dfs(pos, segments_left, cur_max):
        nonlocal best
        if cur_max >= best:
            return
        if segments_left == 1:
            # last segment is [pos, n-1]
            cur = inv(pos, n - 1)
            best = min(best, max(cur_max, cur))
            return

        for end in range(pos, n - segments_left + 1):
            cur = inv(pos, end)
            dfs(end + 1, segments_left - 1, max(cur_max, cur))

    dfs(0, k, 0)
    return best


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(min_max_inv_bruteforce(a, k))


if __name__ == "__main__":
    main()

