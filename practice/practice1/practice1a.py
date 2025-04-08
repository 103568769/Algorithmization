def find_max(lists):
    return max(max(sublist) for sublist in lists)


def main():

    list1 = [[2, -5], [-2, 3], [-4, 7]]
    list2 = [[-2, 3], [-4, 9], [-1, 7]]

    max1 = find_max(list1)
    max2 = find_max(list2)

    print("Максимальний елемент першого списку: ", max1)
    print("Максимальний елемент другого списку: ", max2)


main()
