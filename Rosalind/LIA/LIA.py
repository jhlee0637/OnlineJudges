from math import comb

def independence(gen, minAaBbChild):
    children = 2 ** gen
    AaBb = 0.25
    result = 0

    for i in range(minAaBbChild):
        p1 = comb(children, i)
        p2 = (AaBb ** i) * ((1 - AaBb) ** (children - i))
        result += p1 * p2

    return 1 - result

if __name__ == "__main__":
    gen, minAaBbChild = 6, 16
    result = independence(gen, minAaBbChild)
    print(round(result,3))