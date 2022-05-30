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

def main():
    t = Polynomial(3, 1, 0, 0, 0)
    x = list(range(5))
    print(t.produceYArray(x))

if __name__ == "__main__": main()