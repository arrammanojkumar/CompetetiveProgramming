if __name__ == '__main__':
    n = int(raw_input())
    arr = list(set(map(int, raw_input().split())))
    arr.sort(reverse=True)
    print(arr[1])
