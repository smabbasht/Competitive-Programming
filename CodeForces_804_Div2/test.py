def main():
    lups = [0,1,2,3,4,5,6,7,8,9,]

    for i in range(10):
        if lups[i]%2==0:
            del(lups, i)
            i-=1

    print(lups)
main()