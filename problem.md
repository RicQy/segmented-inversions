# Segmented Inversions

You are given an array `a` of length `n`. You must cut the array into exactly `k` non-empty contiguous segments.

Formally, you must choose indices

- `1 = l₁ ≤ r₁ < l₂ ≤ r₂ < … < lₖ ≤ rₖ = n`

such that each segment is `[lᵢ, rᵢ]` for `i = 1..k`.

For a segment `[l, r]`, define its **inversion count** as the number of pairs `(i, j)` such that

- `l ≤ i < j ≤ r` and `a[i] > a[j]`.

The **score** of a partition is the maximum inversion count over all its segments.

Your task is to **minimize** this score over all possible ways to partition the array into exactly `k` segments.

Output the minimum possible score.

---

## Input

The first line contains a single integer `T` — the number of test cases.

Each test case consists of two lines:

- The first line contains two integers `n` and `k` (`1 ≤ k ≤ n ≤ 100000`).

- The second line contains `n` integers `a₁, a₂, …, aₙ` (`1 ≤ aᵢ ≤ 10⁹`).

It is guaranteed that the sum of `n` over all test cases does not exceed `200000`.

---

## Output

For each test case, output a single integer — the minimum possible value of the maximum inversion count among the `k` segments.

---

## Examples

### Example 1

**Input**

```
1

3 1
3 1 2
```

**Output**

```
2
```

**Explanation**

We must use a single segment `[1, 3]`.  

Its inversion count is `2` (pairs `(1, 2)` and `(1, 3)`), so the score is `2`.

---

### Example 2

**Input**

```
1

4 2
4 3 2 1
```

**Output**

```
1
```

**Explanation**

One optimal partition is `[4, 3] | [2, 1]`.

- Segment `[4, 3]` has `1` inversion.

- Segment `[2, 1]` has `1` inversion.

So the score is `max(1, 1) = 1`, and it is impossible to get a score of `0`.

---

### Example 3

**Input**

```
1

5 5
5 4 3 2 1
```

**Output**

```
0
```

**Explanation**

We can take each element as a separate segment, so every segment has `0` inversions and the score is `0`.

