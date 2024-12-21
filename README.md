# The Bisection Algorithm

I learned an interesting algorithm during my university studies called the **bisection algorithm**. This algorithm is used to approximate the logarithm base 10 (\(\log_{10}\)) of a number by narrowing down the interval where the solution lies.

## How It Works

The bisection algorithm works by iteratively refining an interval that contains the value of \(\log_{10}(a)\). It starts with two points, \(L\) (lower bound) and \(U\) (upper bound), where:

- \(L = 0\)
- \(U = a\)

The algorithm then calculates the midpoint:

\[
x = \frac{L + U}{2}
\]

The function \(10^x\) is evaluated at \(x\). Depending on whether \(10^x\) is greater than or less than \(a\), the interval is updated:

- If \(10^x > a\), update \(U = x\).
- Otherwise, update \(L = x\).

This process is repeated until the relative error between \(10^x\) and \(a\) is less than a specified threshold (e.g., \(10^{-10}\)). The final value of \(x\) approximates \(\log_{10}(a)\).

## Implementation

Here, I will share the implementation of the bisection algorithm to approximate \(\log_{10}(a)\) in Python:

```python
def bisection_log10(a):
    L, U = 0, a
    x = (L + U) / 2
    while abs(10**x - a) > 1e-10 * a:
        if 10**x > a:
            U = x
        else:
            L = x
        x = (L + U) / 2
    return x

# Example usage
a = float(input("Enter a number: "))
result = bisection_log10(a)
print(f"The approximate log10({a}) is {result}")
```

