# Solution – Segmented Inversions

## 1. Definitions

Given an array `a[1..n]` and an integer `k`, we must partition the array into exactly `k` non-empty contiguous segments:

- `1 = l₁ ≤ r₁ < l₂ ≤ r₂ < … < lₖ ≤ rₖ = n`.

For a segment `[l, r]`, define:

\[
\text{inv}(l, r) = \# \{ (i, j) \mid l \le i < j \le r,\, a[i] > a[j] \}.
\]

The score of a partition is:

\[
\max_{1 \le s \le k} \text{inv}(l_s, r_s).
\]

We want to minimize this score.

---

## 2. Observations

1. **If `k ≥ n`**:

   We can make each element a separate segment.  

   Each segment has zero inversions, so the answer is `0`.

2. **Answer range**:

   - Minimum possible score: `0`.

   - Maximum possible score: total number of inversions in the entire array, call it `TOT`.

   - So the answer is in `[0, TOT]`.

3. **Monotonicity for binary search**

   For a fixed integer `X`, define:

   > `P(X)`: It is possible to partition the array into **at most** `k` segments such that each segment has at most `X` inversions.

   This predicate is **monotone**:

   - If `P(X)` is true, then for any `Y ≥ X`, `P(Y)` is also true (looser bound).

   - Therefore we can **binary search** over `X` in `[0, TOT]` to find the smallest `X` such that `P(X)` holds.

   Note: If we can partition into at most `k` segments with per-segment inversions ≤ `X`, then we can always split some segments further to get **exactly** `k` segments without increasing the maximum inversion count.

---

## 3. Greedy Check for Fixed `X`

To check `P(X)`:

> Can we partition `a` into at most `k` segments so that each segment has at most `X` inversions?

**Greedy strategy:**

- Start from the left, create segments as long as possible:

  - Begin a new segment at index `curL`.

  - Extend it to the right one element at a time.

  - Track the inversion count inside the current segment.

  - If adding the next element would make the inversion count > `X`, we cut before that element and start a new segment.

Algorithmically:

- `segments = 1`

- Current segment initially empty.

- For each `a[i]` from left to right:

  - Let `extra` be the number of elements already in this segment that are greater than `a[i]`.

  - If `current_inversions + extra > X`:

    - Close current segment at `i-1`.

    - Start new segment at `i`.

    - Reset `current_inversions = 0` and clear the data structure.

    - Insert `a[i]`.

  - Else:

    - `current_inversions += extra`,

    - insert `a[i]`.

At the end:

- If `segments ≤ k`, then `P(X)` is true.

- Otherwise, `P(X)` is false.

**Why is this greedy optimal for fixed `X`?**

- For any `X`, the maximal length of the first segment that respects the limit is uniquely determined.

- Cutting earlier can only increase the number of segments.

- Making each segment as long as possible minimizes the number of segments for that `X`.

---

## 4. Counting "extra" Inversions Efficiently

For each current segment, we need:

> For the new element `a[i]`, how many elements already present are greater than `a[i]`?

Use a **Fenwick Tree (BIT)** with coordinate compression:

1. **Coordinate compression**

   - Collect all distinct values of `a`.

   - Sort them and map each to index `1..m`.

   - Replace `a[i]` with compressed `c[i]`.

2. **Fenwick tree**

   Let `BIT[x]` store the count of elements with compressed value `x` currently in the segment.

   - Insert value `v`: `add(v, +1)`.

   - Count values ≤ `v`: `prefix_sum(v)`.

   - Count values > `v`:

     - `extra = prefix_sum(m) - prefix_sum(v)`.

3. **Lazy clearing between segments**

   Clearing BIT array of size `m` every time is too slow.

   We use a **versioned BIT**:

   - Arrays `bit[1..m]` and `last_ver[1..m]`, plus global `cur_ver`.

   - To "clear", increment `cur_ver`.

   - When touching index `i`:

     - If `last_ver[i] != cur_ver`, treat `bit[i] = 0`, set `last_ver[i] = cur_ver`.

   - This avoids O(m) clearing.

Each greedy check is `O(n log m)`.

---

## 5. Overall Complexity

- Coordinate compression: `O(n log n)`.

- Total inversions `TOT`: one pass with BIT: `O(n log n)`.

- Binary search over `X`:

  - At most ~`log₂(TOT)` iterations (`TOT ≤ n(n-1)/2`).

- Each check: `O(n log n)` using versioned BIT.

Total per test:

\[
O\big(n \log n \cdot \log \text{TOT}\big)
\]

With `∑n ≤ 2·10⁵`, this fits comfortably in `2` seconds and `256MB` in Python with care.

---

## 6. Edge Cases

- `k = n`: answer `0`.

- `n = 1`: answer `0`.

- Repeated values: equal values don't count as inversions, compression handles them.

---

## 7. Summary

For each test case:

1. Read `n`, `k`, `a`.

2. If `k ≥ n`, print `0` and continue.

3. Coordinate-compress `a`.

4. Use Fenwick to compute total inversions `TOT`.

5. Binary search `X` in `[0, TOT]`:

   - For each `X`, run greedy check with versioned BIT.

6. Print the smallest `X` that passes the check.

