def func(lst): #define the outer function as func() and provide the argument lst for list
    f_list = [] #create a blank list called l_list that will be used to record elements that are sub-lists
    def remove_int(lst): #define the first function, which operates to record elements in lst that are sub-lists
        nonlocal f_list #define f_list as a nonlocal variable so that when f_list is changed in the first function, it will be changed in the entire program
        for i in lst: #initiate for to iterate through elements in the list
            if isinstance(i, int): #logical operator to determine if an element is a int.
                True #space filler because ifs require a statement. True does nothing.
            elif isinstance(i, list): #logical operator to determine if an element is a list. If so, the element will be recorded in f_list.
                f_list.append(i) #record sub-list element in f_list.
    def check_list(): #define the second function, which operates by removing list elements from f_list and evaluating them in the first function
        while True: #initiate while loop
            e = f_list[0] #records element at index 0 in f_list as e (popped list)
            f_list.pop(0) #pops the element at index 0 in f_list
            remove_int(e) #sends e to the first function to select all sub-lists and append them to f_list
            if len(f_list) == 0: #terminator condition, if the length of f_list is zero then the loop is complete.
                e = [i + 1 for i in e] #add 1 to each element in the most nested list to make the final list
                print(e) #print the final list
                break
    remove_int(lst) #initiates the first function
    check_list() #initiates the second function (recursive function)

func(input_list) #initiates the entire program