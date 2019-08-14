def factors(n):
    results = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i not in results:
                results.append(i)
            if int(n/i) not in results:
                results.append(int(n/i))
    if n in results:
        results.pop(results.index(n))
    return results