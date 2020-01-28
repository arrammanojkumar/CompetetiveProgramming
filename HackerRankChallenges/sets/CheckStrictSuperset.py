# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    main_set = set(raw_input().split(" "))
    print(all(main_set > set(input().split()) for _ in range(int(input()))))
