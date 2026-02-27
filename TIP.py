#Problem 10, exposing superman, Breakout 80

# bi to be consistant
# ai = bi , return -1
# if n<=0 return -1
# if bi is negative return -1
# if trust is empty return -1


# nested for loop


def expose_superman(trust, n):
    list1 =[]
    if n <= 0 :
        return -1
    for r in trust:
        if r[0] == r[1]:
            return -1
        else:
            list1.append(r[1])
    #check if all values are the same
    if len(set(list1)) == 1:
        return list1[0]
    return -1




    

