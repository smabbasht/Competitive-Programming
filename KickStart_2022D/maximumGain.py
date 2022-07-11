def proceedForOneOnly(O, k, gainOne):
    if k==0:
        return 0
    # print("k:",k , "GainExcp:", gainOne, O) 
    return gainOne + max([proceedForOneOnly(O[1:], k-1, O[0]), proceedForOneOnly(O[:-1], k-1, O[-1])])

def maxGain(A, B, k, gain):
    if k==0:
        return 0
    # print("k:",k , "GainNorm:", gain, A, B)
    if len(B)==0:
        return proceedForOneOnly(A, k-1, gain)
    elif len(A)==0:
        return proceedForOneOnly(B, k-1, gain)
    # print("k:",k , "GainNorm:", gain, A, B)
    return gain + max([maxGain(A[1:], B, k-1, A[0]), maxGain(A[:-1], B, k-1, A[-1]), maxGain(A, B[1:], k-1, B[0]), maxGain(A, B[:-1], k-1, B[-1])])

def main():
    n = int(input())
    for i in range(n):
        nA = int(input()); A = list(map((lambda i: int(i)), input().split()))
        nB = int(input()); B = list(map((lambda i: int(i)), input().split()))
        k  = int(input())
        print(f"Case #{i+1}: {maxGain(A, B, k+1, 0)}")

main()

