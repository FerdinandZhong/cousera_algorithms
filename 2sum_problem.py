import sys
import os
from itertools import islice
from bisect import bisect_left, bisect_right

def insert_nums_into_python_ht(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            num_dict[num] = num_dict[num] + 1
        else:
            num_dict[num] = 1
    return num_dict

# O(20001n) -> O(n) problem is every iteration needs to loop through 20001 numbers
def count_sum(num_dict):
    total_nums = set()
    for x in num_dict.keys():
        # if num_dict[x] == 1 and (t - x) in num_dict and num_dict[t-x] == 1  :
        left = - 10000 -x
        right = 10000 - x
        # print("left {} right {}".format(left, right))
        for t in range(left, right+1, 1):
            if t in num_dict and x != t:
                # print("t: {}, x: {}, y: {}".format(t, x, t-x))
                total_nums.add(x + t)
    return len(total_nums)

# referred function without hash table
def compute_values(_array):
    target_values = set()
    for num in _array:
        low = bisect_left(_array, -10000 - num)
        high = bisect_right(_array, 10000 - num)
        # print("low: {}， high: {}".format(low, high))
        for pair_num in _array[low:high]:
            # print("pair_num: {}".format(pair_num))
            if pair_num != num:
                target_values.add(num + pair_num)
                # print(target_values)
    return len(target_values)

# target: find total number of target values
if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    with open(BASE_DIR + '/data/algo1-programming_prob-2sum.txt') as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    # content = [1, 4, 45, 6, 10, 10, 8]
    num_dict = insert_nums_into_python_ht(sorted(content))
    print(list(islice(num_dict.items(), 10)))
    print(count_sum(num_dict))
    # print(compute_values(sorted(content)))