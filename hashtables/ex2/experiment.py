#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2 , ticket_3 ]

length = len(tickets)
print(length)

dictt = {}
for i in tickets:
    dictt[i.source] = i.destination

print(dictt)



final_list = [dictt['NONE']]

for i in range(len(tickets) - 2):
    next_ticket = dictt[final_list[i]]
    final_list.append(next_ticket)
    print(final_list)
    
    if i == len(tickets) - 3:
        final_list.append('NONE')
        print(final_list)
    
    

