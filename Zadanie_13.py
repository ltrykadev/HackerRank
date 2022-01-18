def sqrt(x, n=10):
    if x > 0:
        result = 1
        while abs(result**2 - x):
            result = 0.5 * (result + x/result)
            print(result)
        return result
    elif x == 0:
        return 0
    else:
        return None

if __name__ == '__main__':
    x = int(input('x: '))
    r = sqrt(x)
    print(f'sqrt(x) = {r}')
