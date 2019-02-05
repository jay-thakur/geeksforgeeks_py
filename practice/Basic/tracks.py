"""
Vishesh, who doesn't like maths, has to certify v-shaped tracks. A track is valid if it satisfies the following conditions :
1. There must be a constant difference between the height of pillars (not zero) of a track. For eg., if the heights of first two pillars are 7 and 5, then height of 3rd pillar must be 3. As 7-5=2 & 5-3=2.
2. The height of middle pillar must be always 1.
3. Number of pillars on the left side must be equal to the number of pillars on the right side of middle pillar. And their heights must be also equal. for example: Track with pillar heights [3 2 1 2 3] is a valid track.
Help him in finding the valid tracks.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting number of pillars and the second line contains N space separated integers which are the heights of pillar.

Output:
Print on the new  line "Yes" if it is a valid v-shaped track. Otherwise, print "No".

Constraints:
1<=T<=100
3<=N<=106
1<=H[i]<=106

Example:
Input:
2
3
2 1 2
5
4 3 2 3 4

Output:
Yes
No
"""


def tracks(arr, size):
    center = size // 2
    h = arr[1] - arr[0]
    c = False
    for i in range(1, len(arr) // 2 + 1):
        if arr[-i] != arr[i - 1]:
            c = False
            break
        elif h == 0:
            c = False
            break
        elif arr[i] - arr[i - 1] != h:
            c = False
            break
        elif arr[center] != 1:
            c = False
            break
        else:
            c = True
    if c:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(tracks(arr, size))
