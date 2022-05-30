# The Basics of Polynomial Expressions

Expressing Polynomial expressions in Python is relatively self-explanatory. As long as you can use the multiplication and power operations, you can create polynomial expressions easily. However, let's first clear up a misconception you may or may not be aware of...

The operator `^` is NOT the power operator. It is the XOR operator (Exclusive OR, used for bytes of data).

Instead, you need to use `**` when expressing powers. Let's use them both and see what they return.

```Python
>>> 3 ^ 2 # XOR
1
>>> 3 ** 2 # Power
9
```

Unless you're implementing bitwise masks in your programs or creating encryption methods, you don't need to worry about XOR.

## Quadratic Expressions

As you've (hopefully) studied at GCSE, you express a quadratic expression as *ax² + bx + c*, or as *(x+a)(x+b)*. Converting this to Python syntax is pretty straightforward, you just need to calculate each part of the expression and sum each result up, like this:

```Python
>>> a, b, c = 1, 2, 3 # Using format ax2 + bx + c
>>> x, y = 3, 0
>>> y = y + (a * (x**2))
>>> y = y + (b * x)
>>> y = y + c
>>> print(y)
18
```

```Python
>>> a, b = 1, 2 # Using format (x+a)(x+b)
>>> x, y = 3, 0
>>> y = (x + a) * (x + b)
>>> print(y)
20
```

Then, you should be able to put these into a function easily. Let's use the first example, but we'll define two functions to create a modular design.

```Python
def linearExpression(x, m, c):
    return (x * m) + c

def quadratic(x, a, b, c):
    out = a * (x ** 2)
    out = out + linearExpression(x, b, c)
    return out
```

Note that this only really works when all the arguments used are integers or floating points. If you try using strings or lists, you'll just end up with a new, longer item. You instead need to use a `for` loop for any iterable object.

## Creating Polynomial Expressions

As we've just covered, defining a quadratic expression is relatively simple to do in Python, but let's say we wanted to do a... quartic equation. Let's see how that looks.

```Python
def quartic(x, a, b, c, d, e, f):
    out = a * (x ** 4)
    out += b * (x ** 3)
    out += c * (x ** 2)
    out += d * x
    out += e
    return out
```

Yeah, not great. In case you're wondering why I didn't do this on one line, it would be a mess of brackets. And readability of code is very important.

So, how can we create a polynomial expression where we don't know the largest power yet? A polynomial expression that goes up to power *n* has the form *axⁿ + bxⁿ‾¹ + ... + gx¹ + hx⁰* or *(px + a) * (qx + b) * ... * (tx + h), with n number of brackets.*. So, for expanded form, we can specify the maximum power (AKA *n*), and then provide each coeffiecient for each term. As for factorised form, also specify *n*, then the coefficient of *x* and the accompanying constant for each bracket. But if we don't already know how large *n* is, how do we know how many other arguments to include? We can use `*args`. Let's look at an example by creating a class for binomial expressions.

```Python
class Polynomial():
    def __init__(self, n: int, *args):
        if len(args) != n+1: raise ValueError() # Incorrect number of coefficients
        self.n = n
        self.coefficients = args # Coefficients are stored in descending powers of x
    
    def produceYArray(self, x: list):
        out = []
        for val in x:
            acc = 0
            for i in range(self.n):
                acc += self.coefficients[i] * (val ** (self.n-i))
            out.append(acc)
        return out
```

I have ommitted some very important error-checking here, such as making sure the user only uses floats and integers for each argument past `n`.

Now, let's add an extra bit of code at the end to create a cubic expression...

```Python
t = Polynomial(3, 1, 0, 0, 0)
x = list(range(5)) # [0, 1, 2, 3, 4]
print(t.produceYArray(x))
```

And see what it spits out.

```Python
[0, 1, 8, 27, 64]
```

That seems to check out in comparison to the values of x³. Now, you don't have to do it this way, you could also use a recursive function (A.K.A. a function that calls itself). But this is how you can create polynomial expressions in Python!

> If you can't be asked to copy-paste the code, [here it is...](code.py)
