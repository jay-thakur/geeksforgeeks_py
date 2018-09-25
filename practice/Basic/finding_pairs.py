def finding_pairs(arr, s):
    count = 0
    for j in range(0, len(arr) - 1, 2):
        if arr[j] in s and arr[j + 1] in s:
            count = count + 1
    print(count)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()][0:2]
        size = input()
        arr = [int(i) for i in input().split()][0:size]
        s = input()
        print(finding_pairs(arr, s))