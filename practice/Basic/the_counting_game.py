"""
Shubham wrote a sequence of words in following format,having the following properties:
-It is a concatenation of one or more words consisting of English letters.
-All letters in the first word are lowercase.
-For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
-Given , print the number of words in a new line.
Examples-
String saveChangesInTheEditor contains five words- save, Changes, In, The, Editor .
Thus, we print 5 on a new line.
and iAmShubam contains three words- i, Am, Shubham .
Thus, we print 3 on a new line.
Input Format-
A single line containing string s.
Output Format-
Print the number of words in string .
Constraints-
1<=T<=150
1<=|s|<=100000

Example:
Input-
2
saveChangesInTheEditor
iAmShubam
Sample Output-
5
3
"""


def the_counting_game(s):
    c = 0
    for i in s:
        if i.isupper():
            c = c + 1
    return c + 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(the_counting_game(s))
