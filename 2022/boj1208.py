import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

arr_1 = arr[:n // 2]
arr_2 = arr[n // 2:]

subsum_arr_1 = []
subsum_arr_2 = []

for i in range(len(arr_1) + 1):
    comb_1 = combinations(arr_1, i)
    for comb in comb_1:
        subsum_arr_1.append(sum(comb))

for i in range(len(arr_2) + 1):
    comb_2 = combinations(arr_2, i)
    for comb in comb_2:
        subsum_arr_2.append(sum(comb))

subsum_arr_1.sort()
subsum_arr_2.sort()

left_pointer = 0
right_pointer = len(subsum_arr_2) - 1
ans = 0

while left_pointer < len(subsum_arr_1) and right_pointer >= 0:
    tmp = subsum_arr_1[left_pointer] + subsum_arr_2[right_pointer]

    if tmp == s:
        same_count_left = 1
        same_count_right = 1

        same_left_idx = left_pointer
        same_right_idx = right_pointer

        left_pointer += 1
        right_pointer -= 1

        while left_pointer < len(subsum_arr_1) and subsum_arr_1[left_pointer] == subsum_arr_1[same_left_idx]:
            same_count_left += 1
            left_pointer += 1

        while right_pointer >= 0 and subsum_arr_2[right_pointer] == subsum_arr_2[same_right_idx]:
            same_count_right += 1
            right_pointer -= 1

        ans += same_count_left * same_count_right

    elif tmp < s:
        left_pointer += 1

    else:
        right_pointer -= 1

if s == 0:
    ans -= 1

print(ans)