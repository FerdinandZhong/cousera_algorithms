import sys
import os

def insert_min_heap(current_heap, value, latest_key):
    parent_key = latest_key // 2
    parent = current_heap[parent_key -1]
    # print("parent: {}, parent_key: {}, value: {}, latest_key: {}".format(parent, parent_key, value, latest_key))
    if parent > value:
        if(len(current_heap) >= latest_key):
            current_heap[latest_key -1] = parent
        else:
            current_heap.append(parent)
        current_heap[parent_key -1] = value
        if parent_key == 1:
            return current_heap
        else:
            insert_min_heap(current_heap, value, parent_key)
    else:
        if (len(current_heap) < latest_key):
            current_heap.append(value)
    return current_heap

def insert_max_heap(current_heap, value, latest_key):
    parent_key = latest_key // 2
    parent = current_heap[parent_key -1]
    # print("parent: {}, parent_key: {}, value: {}, latest_key: {}".format(parent, parent_key, value, latest_key))
    if parent < value:
        if(len(current_heap) >= latest_key):
            current_heap[latest_key -1] = parent
        else:
            current_heap.append(parent)
        current_heap[parent_key -1] = value
        if parent_key == 1:
            return current_heap
        else:
            insert_max_heap(current_heap, value, parent_key)
    else:
        if (len(current_heap) < latest_key):
            current_heap.append(value)
    return current_heap

def min_bubble_down(current_heap, parent_key):
    left_child_key = parent_key * 2
    right_child_key = parent_key * 2 + 1
    parent = current_heap[parent_key - 1]
    # print("parent: {}, parent_key: {}, current: {}".format(parent, parent_key, current_heap))
    if right_child_key > len(current_heap):
        if left_child_key > len(current_heap):
            return current_heap
        else:
            left_child = current_heap[left_child_key - 1]
            if parent <= left_child:
                return current_heap
            else:
                current_heap[left_child_key - 1] = parent
                current_heap[parent_key - 1] = left_child
                return current_heap
    left_child = current_heap[left_child_key - 1]
    right_child = current_heap[right_child_key - 1]
    if (parent <= left_child and parent <= right_child):
        return current_heap
    else:
        if left_child <= right_child:
            swapped_key, swapped_child = left_child_key, left_child
        else:
            swapped_key, swapped_child = right_child_key, right_child
        current_heap[swapped_key - 1] = parent
        current_heap[parent_key - 1] = swapped_child
        min_bubble_down(current_heap, swapped_key)
    return current_heap

def max_bubble_down(current_heap, parent_key):
    left_child_key = parent_key * 2
    right_child_key = parent_key * 2 + 1
    parent = current_heap[parent_key - 1]
    if right_child_key > len(current_heap):
        if left_child_key > len(current_heap):
            return current_heap
        else:
            left_child = current_heap[left_child_key - 1]
            if parent >= left_child:
                return current_heap
            else:
                current_heap[left_child_key - 1] = parent
                current_heap[parent_key - 1] = left_child
                return current_heap
    left_child = current_heap[left_child_key - 1]
    right_child = current_heap[right_child_key - 1]
    if (parent >= left_child and parent >= right_child):
        return current_heap
    else:
        if left_child >= right_child:
            swapped_key, swapped_child = left_child_key, left_child
        else:
            swapped_key, swapped_child = right_child_key, right_child
        current_heap[swapped_key - 1] = parent
        current_heap[parent_key - 1] = swapped_child
        max_bubble_down(current_heap, swapped_key)
    return current_heap

def Extract_min(min_heap):
    last_value = min_heap.pop()
    min_value = min_heap[0]
    min_heap[0] = last_value
    min_heap = min_bubble_down(min_heap, 1)
    return min_value, min_heap

def Extract_max(max_heap):
    last_value = max_heap.pop()
    max_value = max_heap[0]
    max_heap[0] = last_value
    max_heap = max_bubble_down(max_heap, 1)
    return max_value, max_heap

def adjust_heap_sizes(min_heap, max_heap):
    if len(min_heap) - len(max_heap) > 1:
        min_value, min_heap = Extract_min(min_heap)
        max_heap = insert_max_heap(max_heap, min_value, len(max_heap) + 1)
        min_heap, max_heap = adjust_heap_sizes(min_heap, max_heap)
    elif len(max_heap) - len(min_heap) > 1:
        max_value, max_heap = Extract_max(max_heap)
        min_heap = insert_min_heap(min_heap, max_value, len(min_heap) + 1)
        min_heap, max_heap = adjust_heap_sizes(min_heap, max_heap)
    return min_heap, max_heap

def get_median(min_heap, max_heap):
    return  max_heap[0] if len(max_heap) >= len(
        min_heap) else min_heap[0]


if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    with open(BASE_DIR + '/data/Median.txt') as f:
        content = f.readlines()
    contents = [int(x.strip()) for x in content]
    # contents = contents[:10]
    # contents = [9, 9, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    min_heap = []
    max_heap = []
    median_total = contents[0]
    if contents[0] >= contents[1]:
        min_heap.append(contents[0])
        max_heap.append(contents[1])
        median_total += contents[1]
    else:
        min_heap.append(contents[1])
        max_heap.append(contents[0])
        median_total += contents[0]
    for value in contents[2:]:
        if value <= max_heap[0]:
            max_heap = insert_max_heap(max_heap, value, len(max_heap) + 1)
        else:
            min_heap = insert_min_heap(min_heap, value, len(min_heap) + 1)
        # print(min_heap, max_heap)
        min_heap, max_heap = adjust_heap_sizes(min_heap, max_heap)
        # print("adjust results: {} {}".format(min_heap, max_heap))
        # print("median: {}".format(get_median(min_heap, max_heap)))
        median_total += get_median(min_heap, max_heap)
    print(median_total)
    print(median_total % (len(min_heap) + len(max_heap)))
