import random

def bubble(li):
    n = len(li)

    for i in range(n):
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

    return li

if __name__ == '__main__':
    li_size = int(input('What size you want the list to be> ? '))

    li = [random.randint(0, 100) for i in range(li_size)]

    sorted_li = bubble(li)
    print(sorted_li)
