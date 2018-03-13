def split_the_string(str):
    if len(set(str)) // 4:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(split_the_string(str))