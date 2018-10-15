"""'
Given two fractions a/b and c/d, compare them and print the larger of the two.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains a single line having a/b and c/d as input. a/b and c/d are separated by a comma and a space.

Ouput:
Print the fraction that is greater. If they are equal, then print "equal" without the quotes.

Constraints:
1<=T<=100
0<=a,c<=1000
1<=b,d<=1000

Example:

Input:
3
5/6, 11/45
8/1, 8/1
2/3, 2/2

Output:
5/6
equal
2/2

Explanation:
For testcase1: 5/6=0.8333... and 11/45=0.2444.... Clearly, 5/6 is greater, so we output it.
For testcase 2: We can see that both the fractions are same, so they are equal.
For testcase 3: 2/3=0.666... and 2/2=1, So, clearly, 2/2 is greater.
"""


def compare_two_fractions(fractions):
    f1 = fractions[0].split('/')
    f1_value = float(f1[0]) / float(f1[1])
    f2 = fractions[1].split('/')
    f2_value = float(f2[0]) / float(f2[1])

    if f1_value > f2_value:
        return fractions[0]
    if f2_value > f1_value:
        return fractions[1]
    else:
        return 'equal'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        fractions = input().split(', ')[0:2]
        print(compare_two_fractions(fractions))
