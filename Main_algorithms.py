items = [1,3,5,7,9,15,24,35,49,50,62,68,75,84]
items2 = [2,9,5,3,8,14,99,4]

def binary_search(items):
    search = int(input("Enter the number you want to find:\n"))
    found = False
    first = 0
    count = 0
    last = len(items) - 1
    while first <= last and found == False:
        midpoint = (first+last) // 2
        if items[midpoint] == search:
            found = True
            count += 1
        else:
            count += 1
            if items[midpoint] < search:
                first = midpoint + 1
            else:
                last = midpoint - 1

    if found == True:
        print("Item was found at position",midpoint+1,"in",count,"searches")
    else:
        print("not in the list bot")

def linear_search(items):
    search = int(input("Enter the value to be searched:"))
    index = 0
    found = False
    while found == False and index <= len(items) - 1:
        if items[index] == search:
            found = True
        else:
            index = index + 1

    if found == True:
        print ("item was found at position",index+1)
    else:
        print("Not in the list lock in BOT")

def bubble_sort(items):
    n = len(items)
    swapped = True
    while n > 0 and swapped:
        swapped = False
        n = n - 1
        for index in range(0,n):
            if items[index] > items[index + 1]:
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
                swapped = True
    print(items)

def insertion_sort(items):
    n = len(items)
    for index in range (1,n):
        current = items[index]
        index2 = index
        while index2 > 0 and items[index2 - 1] > current:
            print(items)
            items[index2] = items[index2 - 1]
            index2 -= 1
        items[index2] = current
    print(items)

def merge_sort(items):
    if len(items) > 1:
        mid = len(items) // 2
        lefthalf = items[:mid]

        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i,j,k = 0,0,0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k] = lefthalf[i]
                i += 1
            else:
                items[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            items[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            items[k] = righthalf[j]
            j += 1
            k += 1

def quick_sort(items):
    if len(items) <= 1:
        return items
    pointer1 = 0
    pointer2 = len(items) - 1
    while pointer1 != pointer2:
        if (items[pointer1] > items[pointer2] and pointer1 < pointer2) or (items[pointer1] < items[pointer2] and pointer1 > pointer2):
            temp1 = items[pointer1]
            items[pointer1] = items[pointer2]
            items[pointer2] = temp1
            temp2 = pointer1
            pointer1 = pointer2
            pointer2 = temp2
        if pointer1 < pointer2:
            pointer1 += 1
        else:
            pointer1 -= 1
    left = quick_sort(items[0:pointer1])
    right = quick_sort(items[pointer1 + 1:len(items)])
    return left + [items[pointer1]] + right

def partition(items,start,end):
    pivot = items[start]
    leftmark = start + 1
    rightmark = end
    done = False
    while not done:
        while leftmark <= rightmark and items[leftmark] <= pivot:
            leftmark += 1
        while items[rightmark] >= pivot and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = items[leftmark]
            items[leftmark] = items[rightmark]
            items[rightmark] = temp
    temp = items[start]
    items[start] = items[rightmark]
    items[rightmark] = temp
    return rightmark

def quick_sort2(items,start,end):
    if start < end:
        split = partition(items,start,end)
        quick_sort2(items,start,split - 1)
        quick_sort2(items, split + 1, end)
    return items


choice = int(input("1: Binary Search || 2: Linear Search || 3: Bubble Sort || 4: Insertion Sort || 5: Merge Sort || 6: Quick Sort || 7: Quick Sort v2\n"))
match choice:
    case 1:
        binary_search(items)
    case 2:
        linear_search(items)
    case 3:
        bubble_sort(items2)
    case 4:
        insertion_sort(items2)
    case 5:
        merge_sort(items2)
        print(items2)
    case 6:
        print(quick_sort(items2))
    case 7:
        print(quick_sort2(items2,0,len(items2) - 1))
    case _:
        print("WRONG, please try again:")
