from trace import CoverageResults


def color_score(X, i):
    score = 1+((X-1)/5)
    print(f"Case #{i+1}: {int(score)}")

def main():
    n = int(input())
    for i in range(n):
        X = int(input())
        color_score(X, i)    
main()

