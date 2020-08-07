
def intersection(arrays):
    list_length = len(arrays)

    dictt = {}

    for listt in arrays:
        for num in listt:
            if num not in dictt:
                dictt[num] = 1
            else:
                dictt[num] += 1
    
    result = []

    dict_items_list = list(dictt.items())

    for item in dict_items_list:
        if item[1] == list_length:
            result.append(item[0])
    

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
