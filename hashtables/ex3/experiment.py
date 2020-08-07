experiment_list = [
    [1,2,3,9],
    [1,4,5,2],
    [1,6,7,2]
]

list_length = len(experiment_list)

dictt = {}

#loop through every list
for listt in experiment_list:
    #loop through each number in each list
    for num in listt:
        #store values in list and increment count
        if num not in dictt:
            dictt[num] = 1
        else:
            dictt[num] += 1
print('dictt', dictt)


#empty list to store common numbers
final_list = []


dict_items_list = list(dictt.items())
print('dict_items list', dict_items_list)

for item in dict_items_list:
    if item[1] == list_length:
        final_list.append(item[0])
print(final_list)