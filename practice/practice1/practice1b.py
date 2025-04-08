list1 = [[2, -5], [-2, 3], [-4, 7]]
list2 = [[-2, 3], [-4, 9], [-1, 7]]


def find_max():
    global list1, list2
    max1 = max(max(sublist) for sublist in list1)
    max2 = max(max(sublist) for sublist in list2)

    print("Максимальний елемент першого списку: ", max1)
    print("Максимальний елемент другого списку: ", max2)


find_max()
