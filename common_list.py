def answer(x, y):
    dict = {}
    for val in x:
        if dict.get(val, None) == None:
            dict[val] = 1
        else:
            dict[val] = dict[val] + 1
            
    for val in y:
        if dict.get(val, None) == None:
            dict[val] = 1
        else:
            dict[val] = dict[val] + 1
    li = []
    for key in dict:
        if dict[key]%2 == 0:
            pass
        else:
            li.append(key)
    return li



if __name__ == '__main__':
    ans = answer([13, 5, 6, 2, 5], [5, 2, 5, 13])
    print ans