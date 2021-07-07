import random

def linear_search(li, obj):
    match = False

    for el in li:
        if el == obj:
            match = True
            break
    
    return match

if __name__ == '__main__':
    li_size = int(input('What size you wish the list to be? > '))
    obj = int(input('What is your objective value? > '))

    li = [random.randint(0, 100) for _ in range(li_size)]

    match = linear_search(li, obj)
    print(f'The element {obj} {"was" if match else "was not"} found in the list.')
