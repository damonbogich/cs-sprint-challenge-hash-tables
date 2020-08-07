#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    dictt = {}

    for ticket in tickets:
      dictt[ticket.source] = ticket.destination
    #put in first fligth
    print(dictt)



    final_list = [dictt['NONE']]


    for i in range(len(tickets) - 2):
        #get destination for where you arrived
      next_trip = dictt[final_list[i]]

      final_list.append(next_trip)


      if i == len(tickets) - 3:
        final_list.append('NONE')
    #none not being added

    return final_list


ticket_1 = Ticket("DCA", "DTW")
ticket_2 = Ticket("NONE", "PDX")
ticket_3 = Ticket("DTW", "NONE") 
ticket_4 = Ticket("PDX", "DCA")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4]

print(reconstruct_trip(tickets, 4))