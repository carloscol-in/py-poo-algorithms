import random

def binary_search(li, obj, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if li[mid] == obj:
        return True
    elif li[mid] < obj:
        return binary_search(li, obj, mid+1, end)
    else:
        return binary_search(li, obj, start, mid-1)

if __name__ == '__main__':
    li_size = int(input('What size you wish the list to be? > '))
    obj = int(input('What is your objective value? > '))

    li = sorted([random.randint(0, 100) for _ in range(li_size)])
    print(li)

    match = binary_search(li, obj, 0, len(li))
    print(f'The element {obj} {"was" if match else "was not"} found in the list.')

