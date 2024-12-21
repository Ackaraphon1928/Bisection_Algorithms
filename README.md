# The Bisection Algorithm

I've learned an interesting algorithm during my university studies called the **bisection algorithm**. This algorithm is used to approximate the Mathematics function (let call *f(x)*) of a number by narrowing down the interval where the solution lies. (It narrowing by 2 times of old interval so it called **bisection**)

## How It Works

The bisection algorithm works by iteratively refining an interval that contains the value of *f(x)*. It starts with two points, **L** (lower bound) and **U** (upper bound).

The algorithm then calculates the midpoint:

let **x = (L+U)/2**

You have to find inverse function of *f(x)* let say *f^-1(x)*

The function *f^-1(x)* is evaluated at x. Depending on whether *f^-1(x)* is greater than or less than **a**, the interval is updated:

- If ***f^-1(x)* > a**, update **U = x**.
- Otherwise, update **L = x**.

This process is repeated until the relative error between *f^-1(x)* and **a** is less than a specified threshold (ex. **10^(-10)**). The final value of **x** approximates ***f(x)***.
