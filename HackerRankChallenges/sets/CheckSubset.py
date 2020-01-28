# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    no_of_tests = int(raw_input())

    for i in range(no_of_tests):
        setA = set()
        setB = set()

        len_set_a = int(raw_input())
        set_a = raw_input().split(" ")
        for j in range(len_set_a):
            setA.add(set_a[j])

        len_set_b = int(raw_input())
        set_b = raw_input().split(" ")
        for j in range(len_set_b):
            setB.add(set_b[j])

        print setA.issubset(setB)
