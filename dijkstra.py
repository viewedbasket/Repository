import math



def dijkstra(graph, start):
    tentative = {}
    confirmed = {}

    confirmed[start] = 0

    #plave the start nodes neighbors in the tentative dictionary
    for node, distance in graph[start].items():
       tentative[node] = distance

    #set next to the node just added to confirmed
    next = start

    #while the tentative dictionary still has nodes
    while tentative:

        shortest_distance = math.inf
       #select node from tentative dictionary with the lowest cost
        for node, distance in tentative.items():
           #determine shortest distance node
           if distance < shortest_distance:
              shortest_distance = distance
              next = node

       #add lowest cost node to confirmed dictionary and update next
        confirmed[next] = shortest_distance
       #remove next node from tentative dictionary
        tentative.pop(next)
       #plave next nodes neighbor on tentative list
        for node, distance in graph[next].items():
            cost = confirmed[next] + distance
       #if the neighbor is not in tentative, add to tentative
       #if the neighbor in tentative, update cost if neccessary
       #if the neighbor in confirmed then ignore
            if node in confirmed:
                continue
            elif (node in tentative) and (cost < tentative [node]):
                tentative[node] = cost
            elif node not in tentative: 
                tentative[node] = cost





def main():
    graph = {
      'A': {'B': 5, 'C':10},
      'B': {'A': 5, 'C': 3, 'D': 11},
      'C': {'A': 10, 'B': 3, 'D':2}, 
      'D': {'B': 11, 'C':2}
   }


    start_node = 'D'

    distances = dijkstra(graph, start_node)

    for node, distance in distances.items:
        print(f"{node} - > {distance}")
   
main()