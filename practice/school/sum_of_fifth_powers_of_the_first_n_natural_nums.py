"""
You will be given a number N. Your task is to find sum of Fifth powers of the first N natural numbers 15 + 25+ 35 + 45+ …….+ N5 till N-th term.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.

Output:
For each test-case, print sum of Fifth powers of the first N natural numbers 15 + 25+ 35 + 45+ …….+ N5 till N-th term.

Constraints:
1<=T<=100
1<=N<=1000

Example:

Input:
3
1
2
3

Output:
1
33
276

Explanation:

For testcase 2: The first 2 natural numbers are 1 and 2. So 15+25=1+32=33
"""


def sum_of_fifth_powers_of_the_first_n_natural_numbers_num(n):
    sum = 0
    for j in range(1, n + 1):
        sum += j ** 5
    return sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_fifth_powers_of_the_first_n_natural_numbers_num(n))
