"""
Rohan and Madhav are playing a Mind game in which  Rohan chooses a Number N (Integer)between 1 To 10 in his mind and Madhav has no idea about the chosen number.

Rohan  is asked to perform the following operations on chosen  number by Madhav.

Step 1:Double the chosen number.

Step 2:Add a number k(even number given as input) to the number obtained after Step1

Step 3:Divide the obtained number in Step 2 by 2.

Step 4:Now subtract the obtained number in Step 3 with the original chosen number N

Madhav's task is to find the answer obtained at the end of Step 4 ,i.e,at the end of all the mentioned operations performed on the number chosen by Rohan.

Help Madhav to find the answer.

Input:

The first line of input contains an integer denoting the number of test cases . Next line of input contains a positive even number K which is to be used in step 2.

Output:

For each test case , the output is in a new line containg an integer which is the required answer at the end of Step 4.

Constraints:
1<=T<=100

2<=K<=1000

K is always even

Example:
Input :

1

10

Output:

5

Suppose rohan choses 3 then after

Step 1:number=6

Step 2:number=6+10=16

Step 3:number=16/2=8

Step 4=8-3=5(required answer).

Example:

Input :

2
4
12

Output :
2
6
"""


def mind_game(n):
    return n // 2


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(mind_game(n))
