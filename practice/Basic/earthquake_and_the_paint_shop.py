"""
Chunky's Paint Shop is one of the famous shop in BantaLand. But 2014 Earthquake caused disarrangement of items in his shop.
Now Chunky wants to retain reputation of his shop, for that he has to arrange items in order.
Each item has 40 digit alpha numeric code .
Your task is to arrange the items in ascending order and print them along with their count.

Input:
First line of the input contains T, the number of test cases. Each line of the test case contains N(no of items) followed by N strings.

Output:
For each test case print the code of sorted items along with their count.

Constraints:
1<=T<=150
1<=N<=29

Example:
Input:
1
5
2234597891 zmxvvxbcij 8800654113 jihgfedcba
1234567891 zxyabcvapo 0123434908 padmadngaa
1234567891 abcdefghij 9876543219 jihgfedcba
2234597891 zmxvvxbcij 8800654113 jihgfedcba
9120121291 zmxvvxbcij 0912114113 mnvxbedcba
Output:
1234567891 abcdefghij 9876543219 jihgfedcba 1
1234567891 zxyabcvapo 0123434908 padmadngaa 1
2234597891 zmxvvxbcij 8800654113 jihgfedcba 2
9120121291 zmxvvxbcij 0912114113 mnvxbedcba 1

Explanation:
We have 5 items here. Each item has a 40 digit alpha-numeric code. We arrange the items based on the lexiographical
order of their alpha-numeric code. The items that are similar are printed only once. The count of the items describes
how many such items are there, so items that appear more than once have their count greater than 1.
"""


def earthquake_and_the_paint_shop(arr):
    arr.sort()
    s = sorted(set(arr))
    for i in s:
        print(i, arr.count(i))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = []
        for i in range(n):
            arr.append(input())
        earthquake_and_the_paint_shop(arr)
