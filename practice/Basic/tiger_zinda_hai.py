"""
Rohan is downloading the movie Tiger Zinda Hai using a torrent website, but he is new to torrent, so he doesn't know the difference between a fake download button and a real download button; therefore, he keeps pressing every button in excitement.
Now he has clicked N  buttons, and many tabs are opened , if a opened tab is clicked again then it closes it.
Your task is to tell how many tabs are open at the end.

Input:
First line consists of T test cases. First line of every test case consists of an integer N. Next line will be the N numbers of Tab clicked or "END" . The "END" button means that all the tabs will be closed.

Output:
Single line output, print how many tabs are open at the end.

Constraints:

1<=T<=100

1<=N<=10000

Example:
Input:
1
5
1 2 1 END 2
Output:
1

Explanation:
In the above test case, firstly tab 1st is opened then 2nd is opened then 1st is closed then all are closed then again 2nd is opened.
"""


def tiger_zinda_hai(arr, n):
    s = []
    t = 0
    for i in range(n):
        if arr[i] == "END":
            s = []
            t = 0
        else:
            if arr[i] not in s:
                s.append(arr[i])
                t = t + 1
            else:
                s.remove(arr[i])
                t = t - 1
    return t


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [i for i in input().split()][0:size]
        print(tiger_zinda_hai(arr, size))
