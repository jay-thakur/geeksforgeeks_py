"""
Ishwar has got N proposals this month, but he is finding it tough to decide which one to accept and which one to reject. So he takes help from Gopal regarding this matter and comes to a conclusion that he will accept two proposals one from his hometown and the other from college.

He gets N roses from N girls , every rose has a number written on it, which describes their popularity.  So, Gopal suggests him to accept the proposal of the girl who gives the rose which has the second maximum number written on it as he is afraid that the girl who gives maximum number written rose might betray him , so he suggests him to accept the proposal of the girl who gives second best number rose for the college and the second minimum one for his hometown as he would be busy enough in college , so he decides to accept the proposal of the second minimum popular girl so that the girl does not leaves him being less popular and he is happy that the girl whose proposal he accepted from hometown is not the least popular girl.

INPUT

The first line contains the number of test cases(T)

First line of each test case contains an integer N number of girls.

Second line of every test case contains N space separated integers representing their popularity.

OUTPUT

Output two numbers , the first number denotes the popularity of the girl whose proposal he has accepted for the college and the second number denotes the popularity of the girl whose proposal he has accepted for hometown.



Constraint:

1<=T<=10

1<=N<=10^5

1<=popularity<=10^6

Sample test cases

2
4
1 2 3 4
5
6 9 1 4 8
Sample output
3 2
8 4
"""


def ishwar_and_his_proposals(arr):
    arr.sort()
    return arr[len(arr) - 2], arr[1]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(*ishwar_and_his_proposals(arr))
