# while loop (pseudocode)
# while the pile isn't empty, grab a box and look through it.
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    empty = 0
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print ("found the key!")

# recursion (pseudocode)
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item) # <-- recursion! because it is a function calling itself.
        elif item.is_a_key():
            print ("found the key!")

# infinite loop recursion.
# def countdown(i):
#     print (i)
#     countdown(i-1)


# recursive function.
def countdown(i):
    print (i)
    if i <= 1: # base case.
        return 
    else : 
        countdown(i-1)
