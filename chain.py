def maximum_fun(n, fun, points):
    # G = {}
    dict1 = {}
    for i in range(n):
        dict1[i] = (fun[i], points[i])

    fun_score = 0; funcp = fun[:]; ppc = points[:]

    while 1:
        all_paths = []
        for i in range(n-1, -1, -1):
            if dict1[i][0]==None:
                continue

            path = []
            cost = 0
            
            j=i
            while(j>=0):
                cost += dict1[j][0]
                j=points[j]

            all_paths.append(sum(path))

    print(fun_score)

'''If I take all paths and then take their max'''


def main():
    n_test = int(input())
    for i in range(n_test):
        n = int(input())
        fun = input.split()
        points = input.split()

        print("Case #"+str(i+1)+": ", end='')
        maximum_fun(n, fun, points)

main()