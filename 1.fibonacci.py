def fibonacci(n):
    if n == 0:
        return True

    previousFibonacci = 0
    currentFibonacci = 1 

    while currentFibonacci <= n:
        if currentFibonacci == n:
            return True

        nextFibonacci = previousFibonacci + currentFibonacci
        previousFibonacci = currentFibonacci
        currentFibonacci = nextFibonacci

    return False

def main():
    n = int(input("Entre um número para saber se é um número de Fibonacci: "))
    print(f"{n} " + ("não " if not fibonacci(n) else "") + "é um número de Fibonacci!")


if __name__=='__main__':
    main()