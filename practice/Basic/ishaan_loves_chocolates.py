"""
As we know, Ishaan has a love for chocolates. He has bought a huge chocolate bar which contains N chocolate squares. Each of the square has a tastiness level which is denoted by an array A[].
Ishaan can eat the first or the last square of the chocolate at once. Ishaan has a sister who loves chocolates too and she demands the last chocolate square. Now, Ishaan being greedy eats the more tasty square first.
Determine the tastiness level of the square which his sister gets.

Input :
First line of input contains a single integer T denoting the number of test cases.
The first line of each test case contains an integer N.
The second line contains N space-separated integers denoting the array A.

Output :
For each test case, print the required answer in a new line.

Constraints :
1 <= T <= 100
1 <= N <= 250
1 <= A[i] <= 1000

Example :
Input :
3
5
5 3 1 6 9
6
2 6 4 8 1 6
4
2 2 2 2
Output :
1
1
2

Explaination :
Case 1 :
Initially : 5 3 1 6 9
5 3 1 6
5 3 1
3 1
1

Case 2 :
Initially : 2 6 4 8 1 6
2 6 4 8 1
6 4 8 1
4 8 1
8 1
1

Case 3 :
Initially : 2 2 2 2
2 2 2
2 2
2
"""


def ishaans_loves_chocolates(arr):
    return min(arr)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(ishaans_loves_chocolates(arr))
