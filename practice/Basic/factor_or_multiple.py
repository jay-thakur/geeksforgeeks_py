"""
Given an array A comprising of N non-zero, positive integers and an integer X, find the logical OR of all such elements in the array that are a multiple of X. The result of OR operation should be printed in decimal form. If there is only one multiple of X in A, print the element in decimal form. If no multiple of X is found, print 0.

Input:

First line of input is an integer T, denoting the number of test cases. For each test case, first line of input is the integer N, the size of array A and the integer X, the factor. Second line comprises of N space separated integers of the array.

Output:

There is only one line of output for each test case, the decimal form of the logical OR of all the binary forms of the multiples of X that occur in A.

Constraints:

1<=T<=100
1<=N<=30
1<=X<=10
1<=A[i]<=100, where i denotes index of the array

Example:

Input:

3
4 2
3 4 3 9
5 3
9 3 1 6 1
3 8
1 2 3

Output:

4
15
0

Explanation:

In the first test case, the only multiple of 2 in array is 4. Hence it is printed.

In the second test case, 9,3 and 6 are multiples of 3. The logical OR of the binary forms of the three gives 1111, which on decimal conversion gives 15. Hence 15 is printed.

In the third test case, there is no multiple of 8 in the array. Hence 0 is printed.
"""


def factor_or_multiple(arr, x):
    res = [num for num in arr if num % x == 0]
    ans = 0
    for num in res:
        ans |= num
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x = [int(i) for i in input().split()][0:2]
        arr = [int(i) for i in input().split()][0:n]
        print(factor_or_multiple(arr, x))
