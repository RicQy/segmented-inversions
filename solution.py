import sys

def solve():
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        if k >= n:
            # Each element can be its own segment -> zero inversions
            print(0)
            continue

        # Coordinate compression
        vals = sorted(set(a))
        m = len(vals)
        comp = {v: i + 1 for i, v in enumerate(vals)}  # 1-based indices for Fenwick
        c = [comp[x] for x in a]

        # Fenwick tree for total inversion count
        BIT = [0] * (m + 2)

        def bit_add(i):
            while i <= m:
                BIT[i] += 1
                i += i & -i

        def bit_sum(i):
            s = 0
            while i > 0:
                s += BIT[i]
                i -= i & -i
            return s

        # Compute total inversions in the whole array
        total_inv = 0
        for x in reversed(c):
            # count how many smaller elements are already seen
            total_inv += bit_sum(x - 1)
            bit_add(x)

        # Binary search on the answer X
        lo, hi = 0, total_inv

        # Versioned Fenwick tree for segment-wise counts
        last_ver = [0] * (m + 2)
        bit = [0] * (m + 2)
        cur_ver = 0

        def clear_tree():
            nonlocal cur_ver
            cur_ver += 1

        def add(i):
            """Add 1 at index i in the current version."""
            v = cur_ver
            while i <= m:
                if last_ver[i] != v:
                    last_ver[i] = v
                    bit[i] = 0
                bit[i] += 1
                i += i & -i

        def pref(i):
            """Prefix sum up to i in the current version."""
            v = cur_ver
            s = 0
            while i > 0:
                if last_ver[i] != v:
                    last_ver[i] = v
                    bit[i] = 0
                s += bit[i]
                i -= i & -i
            return s

        while lo < hi:
            mid = (lo + hi) // 2  # candidate maximum inversions per segment
            clear_tree()
            segments = 1
            cur_inv = 0

            for x in c:
                # how many current elements are greater than x?
                greater = pref(m) - pref(x)
                if cur_inv + greater > mid:
                    # start a new segment at this element
                    segments += 1
                    clear_tree()
                    cur_inv = 0
                    add(x)
                else:
                    cur_inv += greater
                    add(x)

            if segments <= k:
                hi = mid
            else:
                lo = mid + 1

        print(lo)


if __name__ == "__main__":
    solve()

