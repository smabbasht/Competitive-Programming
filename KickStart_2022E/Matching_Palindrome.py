def is_palindrome(string):
    return string[:(len(string)-2)//2:-1] == string[:(len(string)+1)//2]

def matching_palindrome():
    length = int(input()); P = input()
    for index in range(len(P)):
        if is_palindrome(P+P[:index+1]): 
            return P[:index+1]

def main():
    n = int(input())
    for i in range(n):
        Q = matching_palindrome()
        print(f"Case #{i+1}: {Q}")
main()