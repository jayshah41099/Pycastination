from itertools import permutations

def allpermutations(str):

    # store all permutation in list
    permList = permutations(str)
    for perm in list(permList):
        print(''.join(perm))

def permutations(str, current_permutation=""):
    if not str:
        print(current_permutation)
        return

    for i in range(len(str)):
        new_str = str[:i] + str[i + 1:]
        new_permutation = current_permutation + str[i]
        permutations(new_str, new_permutation)

if __name__ == '__main__':
    str = input("enter your string: ")
    permutations(str)
