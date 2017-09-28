def missing_number(lst, max_n):


    set_l = set(lst)

    for n in range(1, max_n+1):
        if n not in set_l:
            return n