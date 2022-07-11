def initializer(col):
    init_str = ".." + "+-"*(col-1) + "+" + "\n" + "|."*(col) + "|" + "\n"
    print(init_str, end="")

def lines_maker(col):
    line_str = "+-"*col + "+" + "\n"
    print(line_str, end="")

def gap_maker(col):
    gap_str = "|."*col + "|" + "\n"
    print(gap_str, end="")

def main():
    n_test = int(input())
    for i in range(n_test):
        print("Case #"+str(i+1)+":")
        row, col = input().split()
        row = int(row); col = int(col)
        initializer(col)
        for _ in range(row-1):
            lines_maker(col)
            gap_maker(col)
        lines_maker(col)

main()
