def xor(x):
    if x%2==1:
        print(-1)
        return
    else:
        print(f"0 0 {int(x/2)}")    
    

def main():
    tests = int(input())
    for i in range(tests):
        n = int(input())
        xor(n)

main()