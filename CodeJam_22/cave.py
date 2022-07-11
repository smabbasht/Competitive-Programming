def cave(rooms, oper):
    passages = 0
    G = {}
    dest = 1
    visited = []

    for i in range(oper+1):
        R, P  = input().split()
        R = int(R); P = int(P)
        G[R] = P
        visited.append(R)
        if dest in visited:
            dest += 1
        print("T", dest, flush=True)
        dest +=1


    R, P = input().split()
    R = int(R); P = int(P)
    G[R] = P
    #print(visited)

    print(G)
    print("E", passages, flush=True)
    return

def main():
    tests = int(input())
    N, K  = input().split()
    N = int(N); K = int(K)
    cave(N, K)

main()