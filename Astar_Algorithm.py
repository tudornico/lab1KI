# This class represent a graph
class Graph:
    # Initialize the class
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict or {}

    # Add a link from A to B of given distance
    def connect(self, a, b, distance):
        self.graph_dict.setdefault(a, {})[b] = distance
        self.graph_dict.setdefault(b, {})[a] = distance

    # Get neighbors or a neighbor
    def get_neighbours(self, a, b):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b, None)


# This class represent a node
class Node:

    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.f < other.f


# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if neighbor == node and neighbor.f >= node.f: 
            return False
    return True


def A_Algorithm(graph, heuristics, start, end):
    open = []
    closed = []

    start_node = Node(start, None)
    goal_node = Node(end, None)

    open.append(start_node)

    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)
        # we are going to add node after node to the closed set
        if current_node == goal_node: # we find the last 
            path = []
            while current_node != start_node: # we remember the path and the heuristics
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            return path[::-1] # returns all

        neighbors = graph.get_neighbours(current_node.name, None) # refresh neighbours

        for key, value in neighbors.items():
            neighbor = Node(key, current_node) # take each node

            if neighbor in closed: 
                continue

            neighbor.g = current_node.g + graph.get_neighbours(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.h +  neighbor.g

            if add_to_open(open, neighbor):
                open.append(neighbor)

    return None


def main():
    graph = Graph({})

    graph.connect("Oslo", "Helsinki", 970)
    graph.connect("Helsinki", "Stockholm", 400)
    graph.connect("Oslo", "Stockholm", 570)
    graph.connect("Stockholm", "Copenhagen", 522)
    graph.connect("Copenhagen", "Warsaw", 668)
    graph.connect("Warsaw", "Bucharest", 946)
    graph.connect("Bucharest", "Athens", 1300)
    graph.connect("Budapest", "Bucharest", 900)
    graph.connect("Budapest", "Belgrade", 316)
    graph.connect("Belgrade", "Sofia", 330)
    graph.connect("Rome", "Palermo", 1043)
    graph.connect("Palermo", "Athens", 907)
    graph.connect("Rome", "Milan", 681)
    graph.connect("Milan", "Budapest", 789)
    graph.connect("Vienna", "Budapest", 217)
    graph.connect("Vienna", "Munich", 458)
    graph.connect("Prague", "Vienna", 312)
    graph.connect("Prague", "Berlin", 354)
    graph.connect("Berlin", "Copenhagen", 743)
    graph.connect("Berlin", "Amsterdam", 648)
    graph.connect("Munich", "Lyon", 753)
    graph.connect("Lyon", "Paris", 481)
    graph.connect("Lyon", "Bordeaux", 542)
    graph.connect("Madrid", "Barcelona", 628)
    graph.connect("Madrid", "Lisbon", 638)
    graph.connect("Lisbon", "London", 2210)
    graph.connect("Barcelona", "Lyon", 644)
    graph.connect("Paris", "London", 414)
    graph.connect("London", "Dublin", 463)
    graph.connect("London", "Glasgow", 667)
    graph.connect("Glasgow", "Amsterdam", 711)
    graph.connect("Budapest", "Prague", 443)
    graph.connect("Barcelona", "Rome", 1471)
    graph.connect("Paris", "Bordeaux", 579)
    graph.connect("Glasgow", "Dublin", 306)

    heuristics = {'Amsterdam': 2280, 'Athens': 1300, 'Barcelona': 2670, 'Belgrade': 630, 'Berlin': 1800,
                  'Bordeaux': 210, 'Budapest': 900, 'Copenhagen': 2250, 'Dublin': 2530, 'Glasgow': 2470,
                  'Helsinki': 2820, 'Lisbon': 3950, 'London': 2590, 'Lyon': 2660, 'Madrid': 3300, 'Milan': 1750,
                  'Munich': 1600, 'Oslo': 2870, 'Palermo': 1280, 'Paris': 2970, 'Prague': 1490, 'Rome': 1140,
                  'Sofia': 390, 'Stockholm': 2890, 'Vienna': 1150, 'Warsaw': 946}

    path = A_Algorithm(graph, heuristics, 'Bucharest', 'Glasgow')
    print(path)


main()
