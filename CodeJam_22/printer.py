def decider(p1, p2, p3, p4):
    c = min(p1); m = min(p2); y = min(p3); k = min(p4)
    total = 1000000
    res = c+m+y+k
    if res >= total:
        max1 = max([c,m,y,k])
        diff = res-total
        if (c==max1):
            lst1 = [c, m, y, k]
            for _1 in range(4):
                diff_inn = diff-lst1[_1]
                if diff_inn >= 0:
                    diff -= lst1[_1]
                    lst1[_1] = diff_inn
                else:
                    lst1[_1] = abs(diff_inn)
            
        elif (m==max1):
            ind = 2
            lst1 = [c, m, y, k]
            for _1 in range(4):
                diff_inn = diff-lst1[_1]
                if diff_inn >= 0:
                    diff -= lst1[_1]
                    lst1[_1] = diff_inn
                else:
                    lst1[_1] = abs(diff_inn)
            
        elif (y==max1):
            ind = 3
            lst1 = [c, m, y, k]
            for _1 in range(4):
                diff_inn = diff-lst1[_1]
                if diff_inn >= 0:
                    diff -= lst1[_1]
                    lst1[_1] = diff_inn
                else:
                    lst1[_1] = abs(diff_inn)
            
        else:
            ind = 4
            lst1 = [c, m, y, k]
            for _1 in range(4):
                diff_inn = diff-lst1[_1]
                if diff_inn >= 0:
                    diff -= lst1[_1]
                    lst1[_1] = diff_inn
                else:
                    lst1[_1] = abs(diff_inn)
        print(lst1[0], lst1[1], lst1[2], lst1[3], sep=", ")    

    else:
        print("IMPOSSIBLE")

def main():
    test_n = int(input())
    for i in range(test_n):
        print("Case "+str(i+1)+": ", end='')
        c1, m1, y1, k1 = input().split()
        c1 = int(c1); m1 = int(m1); y1 = int(y1); k1 = int(k1)
        c2, m2, y2, k2 = input().split()
        c2 = int(c2); m2 = int(m2); y2 = int(y2); k2 = int(k2)
        c3, m3, y3, k3 = input().split()
        c3 = int(c3); m3 = int(m3); y3 = int(y3); k3 = int(k3)
        p1 = [c1, c2, c3]
        p2 = [m1, m2, m3]
        p3 = [y1, y2, y3]
        p4 = [k1, k2, k3]
        decider(p1, p2, p3, p4)

main()