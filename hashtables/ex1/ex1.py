#1. populate dictionary: {value: (index, difference)}
#2. convert dict into list (index = (value, (differrence, index)))


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    dictt = {}
    #populate dict with (val, (index, difference))
    for i in range(len(weights)):
      if (weights[i] in dictt) and (weights[i] == dictt[weights[i]][1]):
        return (i,dictt[weights[i]][0])
      dictt[weights[i]] = (i,limit - weights[i])


    #reverse order so that highest index up front
    sorted_dictt = sorted(dictt.items(), reverse=True, key=lambda x: x[1][0])
    print('sorted dictt', sorted_dictt)

    #loop through reversed list to and check if difference in dict

    # check if              k         k         k            k       dicct{k}
    # sorted_dictt = [(7,(3,2)), (5,(2,4)), (4, (1,5)),  (10, (0,-1))]
    # dictt= {4: (1,5), 5: (2,4), 7: (3,2), 10: {0, -1}}
    
    for item in sorted_dictt:
      if item[1][1] in dictt:
        answer = (item[1][0],dictt[item[1][1]][0])
        print('here',dictt[item[1][1]][0])
        return answer
    
    return None

weights = [10,4,5,7]
length = 4
limit = 9
get_indices_of_item_weights(weights, length, limit)
