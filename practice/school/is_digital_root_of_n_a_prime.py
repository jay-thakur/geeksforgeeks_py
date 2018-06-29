"""
Given a number N, you need to find if its digital root is prime or not. DigitalRoot of a number is the repetitive sum of its digits until we get a single digit number.
Eg.DigitalRoot(191)=1+9+1=>11=>1+1=>2

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains a single line having N as input.

Ouput:
For each testcase, print 1 if the digitalRoot(N) is prime, else print 0.

Constraints:
1<=T<=110
1<=N<=10000

Example:

Input:
3
89
45
12

Output:
0
0
1

Explanation:
For testcase 1: DigitalRoot(89)=>17=>1+7=>8; not a prime.
For testcase 3: DigitalRoot(12)=>1+3=>3; a prime number.
"""


def is_digital_root_a_prime(num):
    prime = (2, 3, 5, 7)
    is_prime = 0

    while len(num) > 1:
        s = 0
        for j in range(len(num)):
            s += int(num[j])
        num = str(s)

    for i in prime:
        if i == int(num):
            is_prime = 1

    return is_prime


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        num = input()
        print(is_digital_root_a_prime(num))
