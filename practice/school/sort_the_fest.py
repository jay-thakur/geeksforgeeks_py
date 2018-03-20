"""
You are the social welfare manager of the fest. Some restaurant owners are also investing in your fest. You are given the menu of the two restaurants. There may be a chance of fight between them if any one of them have any item in common and you surely don't want that to happen. Each of the menu has 5 items (strings) in them. So, your task is to find out if there is any need to change the menu or let them be happy with their respective menu.

Input :
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains 2 lines.The first line of each test case represents the space separated strings denoting the menu of Restaurant A. The second line of each test case represents the menu of Restaurant B.

Output :
For each test case in a new line print without quotes "CHANGE" if there is any clash in the menu, else print "BEHAPPY".

Constraints :
1 ≤ T ≤ 100
Length of each indiviual string ≤ 15

Example:
Input :
2
cake pastry fish candy meat
burger ham fish cake sauce
pizza chicken cake chilli candy
choco coco cabbage panner cheese

Output :
CHANGE
BEHAPPY
"""


def menu_match(first_menu, second_menu):
    menus = list(set(first_menu) & set(second_menu))
    if len(menus) > 0:
        return 'CHANGE'
    else:
        return 'BEHAPPY'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        first_menu = list(map(str, input().split()))
        second_menu = list(map(str, input().split()))
        print(menu_match(first_menu, second_menu))