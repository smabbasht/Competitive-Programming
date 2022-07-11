def main():
    count = 0
    # n = int(input())
    n = 2
    for i in range(n):
        # txt = input()
        txt = "helicopteretpocileh" #sampleInputForPreview
        count += txt == txt[::-1]
    print(count)

main()
