list = [1,3,5,7,9,15,24,35,49,50,62,68,75,84]
list2 = [2,9,5,3,8,14,99,4]

def binary_search(list):
    search = int(input("Enter the number you want to find:\n"))
    found = False
    first = 0
    count = 0
    last = len(list) - 1
    while first <= last and found == False:
        midpoint = (first+last) // 2
        if list[midpoint] == search:
            found = True
            count += 1
        else:
            count += 1
            if list[midpoint] < search:
                first = midpoint + 1
            else:
                last = midpoint - 1

    if found == True:
        print("Item was found at position",midpoint+1,"in",count,"searches")
    else:
        print("not in the list bot")

def linear_search(list):
    search = int(input("Enter the value to be searched:"))
    index = 0
    found = False
    while found == False and index <= len(list) - 1:
        if list[index] == search:
            found = True
        else:
            index = index + 1

    if found == True:
        print ("item was found at position",index+1)
    else:
        print("Not in the list lock in BOT")

def bubble_sort(list2):
    n = len(list2)
    swapped = True
    while n > 0 and swapped:
        swapped = False
        n = n - 1
        for index in range(0,n):
            if list2[index] > list2[index + 1]:
                temp = list2[index]
                list2[index] = list2[index + 1]
                list2[index + 1] = temp
                swapped = True
    print(list2)

choice = int(input("1: Binary Search || 2: Linear Search || 3: Bubble Sort\n"))
if choice == 1:
    binary_search(list)
if choice == 2:
    linear_search(list)
if choice == 3:
    bubble_sort(list2)