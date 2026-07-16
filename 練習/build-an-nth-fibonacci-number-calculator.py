def sequence():
    fibonacci = [0, 1]
    return fibonacci

fibonacci_list = [0, 1]

def fibonacci(n):
    if n < len(fibonacci_list):
        return fibonacci_list[n]
    
    for i in range(len(fibonacci_list), n + 1):
        next_val = fibonacci_list[i - 1] + fibonacci_list[i - 2]
        fibonacci_list.append(next_val)
        
    return fibonacci_list[n]

###Alternative answer:

def fibonacci(n):
    sequence = [0,1]
    if n<=1:
        return sequence[n]
    i = 1
    while i<n:
        sequence.append(sequence[i] + sequence[i-1])
        i += 1
    return sequence[n]

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))