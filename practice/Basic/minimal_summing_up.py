"""
For a positive, non-zero integer N, find the minimum count of numbers of the form X^(i-1), where X is a given non-zero, non-negative integer raised to the power i-1 (1<=i<=12), so that they sum up to form the number N exactly.

Input:

First line of input is an integer T denoting the number of test cases. For each test case, there are further two lines of input. First line comprises the integer N and second line comprises the integer X, for which any value of i can be taken in its power to satisfy the condition.

Output:

The only line of output is the minimum number of values of X^(i-1), with any value of i in the range 1 to 12, which sum up to the number N exactly. If a particular value of X^(i-1) is taken up two or more times, the count considered will be two or more respectively.

Constraints:

1<=T<=100
2<=X<=5
1<=N<10^8

Example:

Input:

4
10
2
38
3
1005
5
99999999
4

Output:

2
4
5
45

Explanation:

In the first test case, N=10 and X=2, which means the sum of 10 has to be made out of possible values of 2^(i-1).
1+1+1+1+1+1+1+1+1+1=10 , count is 10 here. (1=2^(1-1))
1+1+1+1+1+1+1+1+2=10 , count is 9 here. (2=2^(2-1))
1+1+1+1+1+1+4=10, count is 7 here. (4=2^(3-1))
1+1+8=10, count here is 3. (8=2^(4-1))
2+8=10, count is 2 here, which is minimum of all. Therefore, the output is 2. Similarly, all other results are to be found.

Data type int will be insufficient to store a value as large as 99999999, therefore you can use long int or long long int instead.
"""


def minimal_summing_up(n, x):
    powers = [x ** (i - 1) for i in range(12, 0, -1)]
    i = 0
    d = n
    sums = []
    while d > 0:
        while powers[i] > d:
            i += 1
        sums.append(i)
        d -= powers[i]
    return len(sums)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        x = int(input())
        print(minimal_summing_up(n, x))
