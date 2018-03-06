"""
Given an array of integers check whether there are two numbers present with given product.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N and a product p.
The second line of each test case contain N number of a[].

Output:
Print Yes if two numbers product is equal to p else No.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 200
0 ≤ a[] ≤ 1000
1 ≤ pro ≤ 2000000

Example:

Input:

2
5 2
1 2 3 4 5
8 46
5 7 9 22 15 344 92 8

Output:

Yes
No
"""


def is_equal_to_product(size, arr, product):
    equal_to_product = False
    for i in range(size):
        for j in range(i, size):
            if arr[i] * arr[j] == product:
                equal_to_product = True

    return equal_to_product


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size, product = [int(i) for i in input().split()][0:2]
        arr = [int(i) for i in input().split()][0:size]
        equal = is_equal_to_product(size, arr, product)
        if equal:
            print('Yes')
        else:
            print('No')