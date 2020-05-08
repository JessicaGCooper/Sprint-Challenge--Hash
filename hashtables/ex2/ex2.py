#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    t = dict()

    for ticket in tickets:
        t[ticket.source] = ticket.destination

    route = []
    route.append(t['NONE'])
    for i in route:
        if i in t and len(route) < length:
            route.append(t[i])
    return route
