"""
Jack is very fond of reading. He reads a lot many pages of books in a day. Since he is obsessed with reading, he reads K times more pages than the number of pages he read the previous day.
He read 1 page on the first day. He wants to see that on any given day N, how many pages will he read.
Since the answer can be very large, print the answer in modulo 10^9+7.

Input :
First line of input contains a single integer T denoting the number of test cases.
The first line of each test case contains 2 space-separated integers N and K.

Output :
For each test case, print the required answer in a new line.

Constraints :
1 <= T <= 200
1 <= N <= 250
1 <= K <= 50

Example :
Input :
3
5 2
2 3
3 4
Output :
16
3
16

Explaination :
Case 1 :
On Day 1 : 1
On Day 2 : 2
On Day 3 : 4
On Day 4 : 8
On Day 5 : 16

Case 2 :
On Day 1 : 1
On Day 2 : 3

Case 3 : 
On Day 1 : 1
On Day 2 : 4
On Day 3 : 16
"""


def dull_jack(a, b):
    return (k ** (n - 1)) % (10 ** 9 + 7)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = [int(i) for i in input().split()][0:2]
        print(dull_jack(n, k))
