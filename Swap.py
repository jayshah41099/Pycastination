def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

def main():
    newList = []
    newList = [int(item) for item in input("Enter the list item : ").split()]
    print(swapList(newList))

if __name__ == '__main__':
    main()