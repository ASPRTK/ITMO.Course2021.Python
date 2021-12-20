def flatten(L):
    result = []
    for x in L:
        if type(x) == list:
            result.extend(flatten(x))
        else:
            result.append(x)
    return result

def flatten2(L):
    if type(L) != list:
        return [L]
    else:
        result = []
        for x in L:
            result.extend(flatten2(x))
        return result
    
if __name__ == "__main__":
    v = [[1, 5], 6, [[2]], [3, [7, 8, [9, 10], [11, 12]]]]
    print(v)
    print(flatten(v))
    print(flatten2(v))
    """
    print(flatten2(2))
    print(flatten(2))
    """
