import random

def merge(li):
    if len(li) > 1:
        mid = len(li) // 2
        left = li[:mid]
        right = li[mid:]

        # recursive call
        print('left')
        merge(left)
        print('right')
        merge(right)

        print('End of recursion')
        print('Left: ', left)
        print('Right: ', right)

        # iterators to walk both sublists
        i = 0
        j = 0
        # iterator for main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li[k] = left[i]
                i += 1
            else:
                li[k] = right[j]
                j += 1

            k += 1

        
        # print('Left: ', left)
        # print('Right: ', right)

        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            li[k] = right[j]
            j += 1
            k += 1
        print('List: ', li)

    return li

if __name__ == '__main__':
    li_size = int(input('What size of list do you want? > '))

    li = [random.randint(0, 100) for _ in range(li_size)]

    print(li)

    sorted_li = merge(li)

    print(sorted_li)
