def factorial(n):
    #print(f"At this call n = {n}")
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r
    
    
def helperFunc(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
        
sum = 0        
num = helperFunc(100)
for i in str(num):
    sum += int(i)
print(sum)