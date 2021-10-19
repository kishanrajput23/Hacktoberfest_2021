# BINARY SEARCH ALGORITHM

""" Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one """

def bin_search(testlist,number):
    mid = len(testlist)//2
    # check if number is present in list if it has only one item
    if len(testlist) == 1:
        if testlist[0] == number:
            return True
        else:
            return False
    elif number == testlist[mid]:
        return True
    elif number < testlist[mid]:
        testlist = testlist[:mid]
        return bin_search(testlist,number)
    else:
        number > testlist[mid]
        testlist = testlist[mid:]
        return bin_search(testlist,number)

testlist = []
list_length = int(input('Enter lenth of list: '))
print('Enter list items (on separate lines): ')

for i in range(list_length):
    value = int(input())
    testlist.append(value)
testlist.sort()
number = int(input('What number are u searching for: '))
print(bin_search(testlist,number))

