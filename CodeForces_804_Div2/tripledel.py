def tripleDel(n, arr):
    tracker = 0
    most = max(set(arr), key=arr.count)
    counter=0

    for i in range(n-2):
        if arr[counter]!=most and arr[counter]!=arr[counter+1]:
            arr.pop(counter)
            arr.pop(counter)
            counter-=1
            print(arr, "for loop, counter:", counter)
        else:
            counter+=1
            # print(counter, end=": c_upd | ")

    
    while any(elem != arr[0] for elem in arr):
        if not (tracker==len(arr)-1):
            if arr[tracker]!=arr[tracker+1]:
                if arr[tracker]!=most:
                    arr.pop(tracker) 
                    arr.pop(tracker)
                    tracker-=1
                    print(arr, "most: up", most)
                    continue
                else:
                    if(tracker<len(arr)-2):
                        if (arr[tracker+1]==arr[tracker+2]):
                            arr.pop(tracker) 
                            arr.pop(tracker)
                            tracker-=1
                            # print(arr, "most: down", most)
                            continue
                    else:
                        arr.pop(tracker) 
                        arr.pop(tracker)
                        
        else:
            if not arr[tracker]==max(set(arr), key=arr.count):
                arr.pop(tracker)
                continue
        tracker+=1
        # print(tracker, ": tracker updated")
    print(len(arr))



def main():
    tests = int(input())
    for i in range(tests):
        n = int(input())
        arr = input().split()
        arr = list(map(lambda i: int(i), arr))
        tripleDel(n, arr)

main()
