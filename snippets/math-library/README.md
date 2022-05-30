# Helpful Functions in math

Just like any other programming language, Python has an external math library that should be pre-installed when you install Python, unless you fiddled with the installation settings, which you probably didn't. The import is self-explanatory.

```Python
import math
```

Or, if you just want a few functions...

```Python
from math import sin
```

Or if you like shorthand, like me...

```Python
import math as m
```

Anyway, enough importing, here are the functions you'll want for A-Level Maths.

## Year 1 Pure

### Surds

Also known as a root, and looks like this: *√3* or *3 ^ ½*. `math` has a square-root function which will give you the exact, decimal value of the square root of whatever value you pass into it.

```Python
>>> math.sqrt(4)
2.0
>>> math.sqrt(3)
1.7320508075688772
```

Ironically, you don't have to use this function to find the square root of something. You can always elevate a number to the power of 0.5 instead. This therefore means you can also do cube roots, 4-roots, and so forth, which `math` cannot do.

```Python
>>> 3 ** 0.5
1.7320508075688772
>>> 64 ** (1/3) # Cube Root
3.9999999999999996
```

### Trigonometry

As you can imagine, there are a few functions you can use in relation to trigonometry, including `sin`, `cos` and `tan`. However, these functions will expect you to give an argument in radians, not degrees. Fortunately, there are functions to convert between the two.

```Python
>>> theta = 90 # Degrees
>>> math.sin(theta)
0.8939966636005579
>>> thetaR = math.radians(theta) # Radians
>>> math.sin(thetaR)
1.0
```

For reverse functions, you can use `asin`, `acos` and `atan`, remembering that these will also output the radians for the values you input, so you will need to convert to degrees afterwards.

```Python
>>> r = math.acos(0)
>>> math.degrees(r)
90.0
```

### Exponentials and Logarithms

Python has a function and constant for *e* which you can use for modelling exponential functions.

```Python
>>> math.e
2.718281828459045
>>> math.exp(2) # Same as e ** 2, but more accurate.
7.38905609893065
```

There are four different functions for logarithms: `log`, `log1p`, `log2` and `log10`. `log` can work in place of the other three functions, but using the other three provide more accurate results.

- `log(x)` - Provides natural log of `x`.
- `log(x, a)` - Provides log of base `a` of `x`.
- `log1p(x)` - Provides natural log of `x + 1`, same as `log(x+1)`
- `log2(x)` - Provides log base 2 of `x`.
- `log10(x)` - Provides log base 10 of `x`.

```Python
>>> math.log(2)
0.6931471805599453
>>> math.log(81, 3)
4.0
>>> math.log1p(1)
0.6931471805599453
>>> math.log2(2048)
11.0
>>> math.log10(100000)
5.0
```

## Miscellaneous

`math` also has a pi constant, so that's a thing.

```Python
>>> math.pi
3.141592653589793
```

> For all of the available functions, check the [official documentation](https://docs.python.org/3.8/library/math.html).
