def straight_finder(n, dices):
    dices.sort()
    value = 0

    for _ in range(n):
        if dices[_] >= (value+1):
            value +=1
    print(value)


def main():
    n_test = int(input())
    for i in range(n_test):
        n = int(input())
        dices = input().split()
        for j in range(len(dices)):
            dices[j] = int(dices[j])
        
        print("Case #"+str(i+1)+": ", end='')
        straight_finder(n, dices)

main()