def print_table(t):
    for i in range(t):
        n = int(input())
        for j in range(1, 11):
            print(j * n, end=' ')
        print()


if __name__ == '__main__':
    t = int(input())
    print_table(t)
