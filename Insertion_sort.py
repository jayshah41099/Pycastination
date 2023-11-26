def insertion_sort(list):
    for i in range (1, len(list)):
        currentnumber = list[i]
        for j in range (i - 1, -1, -1):
            if list[j] > currentnumber:
                list[j], list[j + 1] = list[j + 1], list[j]
            else:
                list[j + 1] = currentnumber
                break

    return list

# list = [6, 4, 8, 5, 2, 1, 10, 3, 9, 7]
# start the first loop in right direction and second loop will go in left from the chosen point.

def main():
    list = [6, 4, 8, 5, 2, 1, 10, 3, 9, 7]
    print (" sorted list: ", insertion_sort(list))

if __name__ == '__main__':
    main()