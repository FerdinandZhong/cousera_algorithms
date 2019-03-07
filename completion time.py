import sys
import os

def substraction_merge_sort(a):
    n = len(a)
    b = a[n // 2:]
    a = a[:n // 2]
    # print('a: {}'.format(a))
    # print('b: {}'.format(b))
    if len(a) > 1:
        a = substraction_merge_sort(a)
    if len(b) > 1:
        b = substraction_merge_sort(b)
    x = 0
    y = 0
    merged = []
    for i in range(len(a) + len(b)):
        if (x >= len(a) or y >= len(b)):
            if (x >= len(a)):
                merged.append(b[y])
                y += 1
            elif (y >= len(b)):
                merged.append(a[x])
                x += 1
        else:
            if ((b[y][0] - b[y][1]) > (a[x][0] - a[x][1])):
                merged.append(b[y])
                y += 1
            elif ((b[y][0] - b[y][1]) == (a[x][0] - a[x][1])):
                if (b[y][0]> a[x][0]):
                    merged.append(b[y])
                    y += 1
                else:
                    merged.append(a[x])
                    x += 1
            else:
                merged.append(a[x])
                x += 1
    return merged

def ratio_merge_sort(a):
    n = len(a)
    b = a[n // 2:]
    a = a[:n // 2]
    # print('a: {}'.format(a))
    # print('b: {}'.format(b))
    if len(a) > 1:
        a = ratio_merge_sort(a)
    if len(b) > 1:
        b = ratio_merge_sort(b)
    x = 0
    y = 0
    merged = []
    for i in range(len(a) + len(b)):
        if (x >= len(a) or y >= len(b)):
            if (x >= len(a)):
                merged.append(b[y])
                y += 1
            elif (y >= len(b)):
                merged.append(a[x])
                x += 1
        else:
            if ((b[y][0] / b[y][1]) >= (a[x][0] / a[x][1])):
                merged.append(b[y])
                y += 1
            else:
                merged.append(a[x])
                x += 1
    return merged

def substraction_ordering(jobs):
    sorted_jobs = substraction_merge_sort(jobs)
    print(sorted_jobs)
    total_length = 0
    completion_times = 0
    for job in sorted_jobs:
        total_length += job[1]
        completion_times += total_length * job[0]
    print(total_length, completion_times)

def ratio_ordering(jobs):
    sorted_jobs = ratio_merge_sort(jobs)
    print(sorted_jobs)
    total_length = 0
    completion_times = 0
    for job in sorted_jobs:
        total_length += job[1]
        completion_times += total_length * job[0]
    print(total_length, completion_times)



if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    with open(BASE_DIR + '/data/jobs.txt') as f:
        content = f.readlines()
    total_numbers = content[0]
    jobs = content[1:]
    jobs = [tuple(int(x) for x in job.split()) for job in jobs]
    substraction_ordering(jobs)
    ratio_ordering(jobs)
