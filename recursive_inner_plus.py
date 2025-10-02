def func(lst): #define the outer function as func() and provide the argument lst for list
    l_list = [] #create a blank list called l_list that will be used to record elements that are sub-lists
    def func_remove_int(lst): #define the first function, which operates to record elements in lst that are sub-lists
        for i in lst: #initiate for to iterate through elements in the list
            if isinstance(i, int): #logical operator to determine if an element is a int. If so, the element will be skipped.
                True #space filler because ifs require a statement. True does nothing. 
            elif isinstance(i, list): #logical operator to determine if an element is a list. If so, the element will be recorded in l_list.
                l_list.append(i) #record sub-list element in l_list.
        return l_list #returns l_list as the output of the first function.
    
    def func_pop_list(lst): #define the second function, which operates by removing list elements from l_list and evaluating them in the first function
            p_list = lst[0] #records element at index 0 in l_list as p_list (popped list)
            lst.pop(0) #pops the element at index 0 in l_list
            func_remove_int(p_list) #sends p_list to the first list select all sub-lists and append them to l_list
            if len(lst) == 0: #terminator condition, if the length of l_list is zero then the loop is complete.
                final_list = [i + 1 for i in p_list] #add 1 to each element in the most nested list to make the final list
                return print(final_list) #return the final list
            return (func_pop_list(l_list)) #recursive step to loop through the second function until all items in l_list have been evaluated
    func_remove_int(lst) #initiates the first function
    func_pop_list(l_list) #initiates the second function (recursive function)

func(input_list) #initates the entire program