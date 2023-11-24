
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1, i, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]

    return list


def main():
    list = [6, 4, 8, 5, 2, 1, 10, 3, 9, 7]
    print (" sorted list: ", bubble_sort(list))

if __name__ == '__main__':
    main()