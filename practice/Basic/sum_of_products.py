"""
Given an array A[ ] of N integers, calculate the sum of "A[i] & A[j]" of all the pairs formed by the given array, where & is the bitwise AND operator.

Input
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
The first line of each test case contains a positve integer N, denoting the length of the array A[ ].
The second line of each test case contains a N space seprated positve integers, denoting the elements of the array A[ ].


Output
Print out the sum of products of all pairs formed by the array.

Constraints
1 <= T <= 100
2 <= N <=30
0 <= A[ ] <= 100

Examples

Input
3
3
5 10 15
4
10 20 30 40
5
20 16 32 50 64

Output
15
46
80

Explanation:
For the above test case
Required Value = (5 & 10) + (5 & 15) + (10 & 15)
                             = 0 + 5 + 10
                             = 15

Expected Complexity
Time: O(N)

"""


def sum_of_products(arr, size):
    sum = 0
    for i in range(size):
        for j in range(i + 1, size):
            sum = sum + (arr[i] & arr[j])
    return sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(sum_of_products(arr, size))
