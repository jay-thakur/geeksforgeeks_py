"""
You have to calculate the output in a way that repeated sum of digits until it is before single digit. Multiply those digits which are producing single digit means a final state.

Example-
Lets take 19 as example ,19 breaks into 1+9=10 then 10 breaks into 1+0=1. 1 is a single digit sum.
But we have to multiply the at last step before ( the producer of 1 is 10 so take digits of 10) so 1*0=0
So , output Becomes 0
Lets take another example as 129, so 129 breaks into 1+2+9 =12  breaks into 1+2=3. 3 is single digit sum.
So we take 12 and multiply its digits 1*2=2
So , output Becomes 2

Input Format-
First Line contains no of test cases by t, and then t inputs.

Output Format-
Every case result should be in new line.

Constraints-
1<=T<=200
1<=n<=4294967296 (232)

Input-
2
19
129

Output-
0
2
"""


def repated_sum_and_then_multiply(n):
    n = list(map(int, str(n)))
    while sum(n) > 9:
        n = list(map(int, str(sum(n))))

    m = 1
    for item in n:
        m *= item

    return m


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(repated_sum_and_then_multiply(n))
