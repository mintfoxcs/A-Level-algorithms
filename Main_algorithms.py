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

def bubble_sort(list):
    n = len(list)
    swapped = True
    while n > 0 and swapped:
        swapped = False
        n = n - 1
        for index in range(0,n):
            if list[index] > list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp
                swapped = True
    print(list)

def insertion_sort(list):
    n = len(list)
    for index in range (1,n):
        current = list[index]
        index2 = index
        while index2 > 0 and list[index2 - 1] > current:
            print(list)
            list[index2] = list[index2 - 1]
            index2 -= 1
        list[index2] = current
    print(list)

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        lefthalf = list[:mid]

        righthalf = list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i,j,k = 0,0,0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i += 1
            else:
                list[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            list[k] = righthalf[j]
            j += 1
            k += 1


choice = int(input("1: Binary Search || 2: Linear Search || 3: Bubble Sort || 4: Insertion Sort || 5: Merge Sort\n"))
match choice:
    case 1:
        binary_search(list)
    case 2:
        linear_search(list)
    case 3:
        bubble_sort(list2)
    case 4:
        insertion_sort(list2)
    case 5:
        merge_sort(list2)
        print(list2)
    case _:
        print("WRONG, please try again:")


