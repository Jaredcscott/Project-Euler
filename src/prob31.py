coins = [1,2,5,10,20,50,100]
ways = 0
for a in range(100):
    for b in range(100):
        for c in range(100):
            for d in range(100):
                for e in range(100):
                    for f in range(100):
                        for g in range(100):
                            if coins[0] * a + coins[1] * b + coins[2] * c + coins[3] * d + coins[4] * e + coins[5] * f + coins[6] * g == 200:
                                ways += 1
                                print(str(a) + "*1p " + str(b) + "*2p " + str(c) + "*5p " + str(d) + "*10p " + str(e) + "*20p " + str(f) + "*50p " + str(g) + "*100p ") 
print(ways)