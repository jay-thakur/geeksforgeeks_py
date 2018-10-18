def if_the_num_is_balanced(n):
    lsum = 0
    rsum = 0
    for i in range(0, int((len(n) + 1) / 2)):
        lsum += int(n[i])
        rsum += int(n[-(i + 1)])
    if rsum == lsum:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(if_the_num_is_balanced(n))
