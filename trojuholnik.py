
def trojuholnik(riadok):
    k = 2 * riadok - 3
    for i in range(0,riadok):
        for j in range(0, k):
            print(" ",end="")
        k -= 1
        for x in range(0,i+1):
            print(("*"), end=" ")
        print("")
trojuholnik(5)
