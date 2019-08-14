fib = [1,1]
while len(str(fib[len(fib) -1])) < 1000:
    nextNum = fib[-2] + fib[-1]
    fib.append(nextNum)
    #print(fib)
    
for i in range(len(fib)-5,len(fib)):
    print("Length: " + str(len(str(fib[i]))))
    print(fib[i])

print(len(fib))
