
def selection_sort(list):
    for i in range (len(list) - 1):
        minimum = i
        for j in range ( i + 1, len(list)):
            if (list[j] < list[minimum]):
                minimum = j
        if minimum != i:
            list[i], list[minimum] = list[minimum], list[i]
            
    return list

def main():
    list = [6, 4, 8, 5, 2, 1, 10, 3, 9, 7]
    print (" sorted list: ", selection_sort(list))

if __name__ == '__main__':
    main()