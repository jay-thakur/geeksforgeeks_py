"""
Ishaan has been learning different representations of numbers, like binary, octal, decimal, etc. He has an assignment of a lot of problems. He is given 2 integers N and K.
Ishaan needs to convert N (given in decimal) and convert it to base K. Help him calculate the answer.

Input :
First line of input contains a single integer T denoting the number of test cases.
The only line of each test case contains 2 space-separated integers N and K.

Output :
For each test case, print the required answer in a new line.

Constraints :
1 <= T <= 200
1 <= N <= 10^9
2 <= K <= 10

Example :
Input :
3
10 2
4 8
15 6
Output :
1010
4
23

Explanation :
Case 1 :
10 in Binary = 1010

Case 2 :
4 in Octal = 4

Case 3 :
15 in Base 6 = 23
"""


def the_number_system(n, k):
    ans = ""
    while n != 0:
        r = n % k
        n = int(n / k)
        ans += str(r)
    return ans[::-1]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = [int(i) for i in input().split()][0:2]
        print(the_number_system(n, k))
