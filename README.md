# The Bisection Algorithm

I learned an interesting algorithm during my university studies called the **bisection algorithm**. This algorithm is used to approximate the root of a function that you are interested in.

## How It Works

The bisection algorithm works by iteratively narrowing down the interval where the root lies. It starts with two points, \(a\) and \(b\), such that the function values at these points have opposite signs (i.e., \(f(a) \cdot f(b) < 0\)). This guarantees the existence of a root between \(a\) and \(b\).

The algorithm then calculates the midpoint:

\[
c = \frac{a + b}{2}
\]

It evaluates the function at \(c\). Depending on the sign of \(f(c)\), the interval is updated to either \([a, c]\) or \([c, b]\), progressively narrowing the search range until the root is approximated to the desired accuracy.

## Implementation

Here, I will share the implementation of the bisection algorithm for some interesting functions.
