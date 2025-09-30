def func(lst): #define the outermost function as func()
    l_list = [] #define l_list as empty list. This variable will serve as a list to which all lists and sublists within the argument list will be appended
    def func_remove_int(lst): #define sub-function 1 func_remove_int() which removed all int types from the argument list
        for i in lst:
            if isinstance(i, int):
                del i
            elif isinstance(i, list):
                l_list.append(i)
        return l_list
    
    def func_pop_list(lst):
            p_list = lst[0]
            lst.pop(0)
            func_remove_int(p_list)
            if len(lst) == 0:
                final_list = [i + 1 for i in p_list]
                return print(final_list)
            return (func_pop_list(l_list))
    func_remove_int(lst)
    func_pop_list(l_list)
