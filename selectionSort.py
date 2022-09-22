# sort an array from smallest to largest

def findSmallest(arr):              # a funcion to find the smallest number in an arr.
    smallest = arr[0]               # stores the smallest value. (in an array as the first index)
    smallest_index = 0              # stores the index of the smallest value (as 0 bc it's the start(?))

    for i in range(1, len(arr)):    # for an index within the range of 1 to the length of the arr:
        if arr[i] < smallest:       # if an index in the arr is smallest:
            smallest = arr[i]       # then that index in the arr is the smallest number.
            smallest_index = i      # and that index will be the new smallest index.
    return smallest_index           # which will return the smallest index.

# now you can use this function to write selection sort.
def selectionSort(arr):                  # sorts and array.
    newArr = []                          # we have a new array defined as newArr.
    for i in range(len(arr)):            # for an index in the range of the length of the array:
        smallest = findSmallest(arr)     # find the smallest element in the array, which will be the named "smallest"
        newArr.append(arr.pop(smallest)) # and adds it to the new array by popping the smallest number from the array and appending it to newArr.
    return newArr

print (selectionSort([5, 3, 6, 2, 10]))  # will sort the array to [2, 3, 5, 6, 10].
