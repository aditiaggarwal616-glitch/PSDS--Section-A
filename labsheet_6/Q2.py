print("Fibonacci Series")
n = 5
a = 1
b = 1
for i in range(n):
    print(a, end=" ") 
    c = a + b
    a = b
    b = c