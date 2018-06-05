"""
Given a Sentence S of length N containing only english alphabet characters, your task is to write a program that converts the given sentence to Snake Case sentence. Snake case is the practice of writing compound words or phrases in which the elements are separated with one underscore character (_) and no spaces, with each element's initial letter usually lowercased within the compound and the first letter either upper or lower caseasentence. For ease keep all the characters in lower case.

Input:
First line of the input contains an integer T, denoting the number of test cases. Then T test case follows. First line of each test case contains an integer N denoting the length of the sentence (including spaces). Then next line contains the N length sentence S containing only english alphabets.


Output:
For each test case output the resultant sentence in snake case on a new line.


Constraints:
1<=T<=103
1<=N<=103

Example:
Input:
2
14
Geeks ForGeeks
21
Here comes the garden
Output:
geeks_forgeeks
here_comes_the_garden
"""


def snake_case(str):
    return str.strip().replace(' ', '_').lower()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        str = input()[0:n]
        print(snake_case(str))
