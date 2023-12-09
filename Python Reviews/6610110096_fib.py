def fibonacci(fb) :
    a, b = 0, 1
    sum = 0
    fibonac = [0, 1]
    for x in range(0, fb-1) :
        sum = a + b
        a = b
        b = sum
        fibonac.append(sum)
    return fibonac
input_number = int(input("Input number of Fibonacci number: "))
print(", ".join(map(str,fibonacci(input_number))))