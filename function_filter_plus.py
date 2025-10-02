def func(lst, n): #define the function as func() and set lst and n as arguments for input list and cuttoff criteria
    out_list = [] #sets out_list as a blank list. This will be the full list to which elements that meet the criteria will be added.
    for i in lst: #initates for loop to look at each element in the input list
        if i > n: #if condition for if the element in the input list is greater than the criteria, do nothing.
            True #spaceholder required after if statement. True does nothing.
        elif i < n: #if condition for if the element in the input list is less than the criteria value
            out_list.append(i) #append the element to out_list (i.e., collect all elements that fit the criteria)
    return out_list #return out_list as an output

func(input_list, n) #function to initiate the program