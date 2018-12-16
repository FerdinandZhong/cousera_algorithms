import sys
import os

def inversion_count(a, count=0):
    n = len(a)
    b = a[n//2:]
    a = a[:n//2]
    # print('a: {}'.format(a))
    # print('b: {}'.format(b))
    if len(a) > 1:
        result = inversion_count(a)
        a = result[0]
        count+=result[1]
    if len(b) > 1:
        result = inversion_count(b)
        b = result[0]
        count+=result[1]
    x=0
    y=0
    merged = []
    for i in range(len(a)+len(b)):
        if(x>=len(a) or y>=len(b)):
            if(x>=len(a)):
                merged.append(b[y])
                y += 1
            elif(y>=len(b)):
                merged.append(a[x])
                x+=1
        else:
            if(b[y]<a[x]):
                merged.append(b[y])
                y += 1
                count += (len(a)-x)
            else:
                merged.append(a[x])
                x += 1
    return merged, count

def test(a):
    count = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[j]<a[i]:
                count += 1
    print('test: {}'.format(count))

if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(__file__))
    with open(BASE_DIR+'/data/integerArray.txt') as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    print(content)
    print(inversion_count(content))
    test(content)