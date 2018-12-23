import sys
import os


def first_e_qs(a, count=0):
    n = len(a)
    count += n - 1
    if (n >= 2):
        pivot = a[0]
        i = 1
        tmp = 0
        for j in range(1, len(a)):
            if pivot > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
                i = i + 1
        tmp = a[i - 1]
        a[i - 1] = pivot
        a[0] = tmp
        print(a[:i - 1], pivot, a[i:], "count: {}, n: {}".format(count, n))
        results = first_e_qs(a[:i - 1])
        final_result = results[0]
        count += results[1]
        final_result.append(pivot)
        results = first_e_qs(a[i:])
        final_result.extend(results[0])
        count += results[1]
        return final_result, count
    else:
        return a, 0


def last_e_qs(a, count=0):
    n = len(a)
    count += n - 1
    if (n >= 2):
        tmp = a[0]
        a[0] = a[n - 1]
        a[n - 1] = tmp
        pivot = a[0]
        i = 1
        for j in range(1, len(a)):
            if pivot > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
                i = i + 1
        tmp = a[i - 1]
        a[i - 1] = pivot
        a[0] = tmp
        print(a[:i - 1], pivot, a[i:], "count: {}, n: {}".format(count, n))
        results = last_e_qs(a[:i - 1])
        final_result = results[0]
        count += results[1]
        final_result.append(pivot)
        results = last_e_qs(a[i:])
        final_result.extend(results[0])
        count += results[1]
        return final_result, count
    else:
        return a, 0


def get_median(a, n):
    position = 0
    if (n % 2 != 0):
        position = ((n + 1) // 2) - 1
    else:
        position = (n // 2) - 1
    first = a[0]
    end = a[n - 1]
    middle = a[position]
    three_nums = first_e_qs([first, middle, end])[0]
    print("three nums: {}".format(three_nums))
    if (first == three_nums[1]):
        return a
    elif (middle == three_nums[1]):
        a[0] = middle
        a[position] = first
        return a
    else:
        a[0] = end
        a[n - 1] = first
        return a


def median_e_qs(a, count=0):
    n = len(a)
    count += n - 1
    if (n >= 2):
        a = get_median(a, n)
        pivot = a[0]
        i = 1
        for j in range(1, len(a)):
            if pivot > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
                i = i + 1
        tmp = a[i - 1]
        a[i - 1] = pivot
        a[0] = tmp
        print(a[:i - 1], pivot, a[i:], "count: {}, n: {}".format(count, n))
        results = median_e_qs(a[:i - 1])
        final_result = results[0]
        count += results[1]
        final_result.append(pivot)
        results = median_e_qs(a[i:])
        final_result.extend(results[0])
        count += results[1]
        return final_result, count
    else:
        return a, 0


if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    with open(BASE_DIR + '/data/QuickSort.txt') as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    result = last_e_qs(content)
    print(result)
    print(len(result[0]))
