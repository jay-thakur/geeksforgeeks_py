"""
One day Jay, on getting his first salary, decides to distribute apples among the poverty-stricken persons.He gave each person 1kg of apples.People are coming in a queue and he makes sure that he gives every person 1 kg of apples only once.Every person is identified by a specific integer.

Given the length of the queue N followed by an array of N integers, denoting the persons in that queue, find the minimum kg's of apples Jay will have to distribute.

Input:

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the length of the coming queue. The second line contains N space-separated integers A1, A2, ..., AN denoting the people in that queue.
Output:

For each test case, output a single line containing the answer.
Constraints:

1 ≤ T ≤ 20
1 ≤ N ≤ 105
1 ≤ Ai ≤ 105
Example:

Input:

2
5
1 1 1 1 1
5
1 2 3 1 2
Output:

1

3

Explanation:

For test case 1, the same person (identified by the integer '1' comes again and again in the queue, but Jay will not give him apples again and again . He gave him apples only once so minimum kg's of apples here required-1kg).
For test case 2, person '1' comes and takes 1kg of apples,then person '2' comes and takes 1kg of apples from Jay and then person '3' comes and he also takes 1kg of apples from Jay, then person '1' again comes but he gets nothing as he has already been awarded apples and so with person '2'.So, minimum kg's of apples require 3kg.
"""


def jays_apples(arr):
    return len(set(arr))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(jays_apples(arr))
