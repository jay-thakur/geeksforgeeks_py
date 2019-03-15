"""
A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1,then the number is a magic number.

Input:
First line of input contains a single integer T, denoting the number of test cases. First line of each test case contains an integer N.


Output:
For each of the test case print whether the number N is "Magic" or "Not Magic"


Constraints:
1<=T<=10^5
1<=N<=10^5


Example:

Input:
2
1234
67

Output
Magic
Not Magic

Explanation:
1234 sums up to 10 which sums upto 1 so its a Magic Number.
67 sums up to 11 which sums upto 2 so its not a Magic Number
"""


def sum_of_digit_modified(n):
    while n // 10 > 0:
        temp = 0
        while n > 0:
            temp += (n % 10)
            n //= 10
        n = temp
    if n == 1:
        return "Magic"
    else:
        return "Not Magic"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_digit_modified(n))
