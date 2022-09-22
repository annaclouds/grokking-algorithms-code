# full code
def binary_search(list, item):

# creating the entire array. declaring low element, declaring high element.
    low = 0                         # low and..                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    high = len(list) - 1            # .. high keep track of which part of the list you'll search in.

# each time, you check the middle element (which is splitting the array in half intervals.) the middle of the arraay is the 'guess'.
    while low <= high:              # while you haven't narrowed it down to one element...
        mid = (low + high) // 2      # ... check the middle element.
        guess = list[mid]          

        if guess == item:           # found the item.
            return mid

# and if the guess is too high, you update high.
        if guess > item:            # your guess is too high.
            high = mid - 1          # you minus 1 because your guess was too high anyways, so this would be your new updated high.

# if the guess is too low, you update accordingly. move onto the next middle.
        # if guess < item:
        else:                       # your guess is too low.
            low = mid + 1           # you plus 1 because your guess was too low anyways, so this would be your new updated low.

    return None                     # this item doesn't exist.

# let's test it!
my_list = [1, 3, 5, 7, 9]


# print statements.
print (binary_search(my_list, 3))    # => 1. remember, lists start at 0. the second slot is index 1.

print (binary_search(my_list, -1))   # => None, "nil" in python. it indicates that item wasn't found.    
