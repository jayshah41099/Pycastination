# Question 1 - replace index 1, 2 and 3 with following numbers and print it out the list. 
# (Don't create new list)

aList = [4, 8, 12, 16]
aList[1:4] = [20,24,28]
print(aList)

# Question 2 - print number 40 using negative indexing
bList = [10, 20, 30, 40, 50]
print (bList[-2])

# Question 3 - print a list discarding starting and end entry 
sampleList = [10, 20, 30, 40, 50]
print(sampleList[-4:-1])

# Question 4 - create a list of 10 Nones using minimalist writing
l = [None] * 10
print (len(l))
print(l)

# Question 5 - print out following list as a single string.
myList = ["Hello", "Python"]
print(" ".join(myList))

#question 6 - empty out the list with one line of code
cList = [10, 20, 30, 40]
del cList[0:4]
print(cList, len(cList))

#Question 7 - multiply the each charcter of list by 2 use minimal writing 
dList = [1, 2, 3, 4, 5, 6, 7]
pow2 = [2* x for x in dList]
print(pow2)

# question 8 - add new number 60 at the end of the list
eList = [10, 20, 30, 40, 50]
eList.append(60)
print(eList)