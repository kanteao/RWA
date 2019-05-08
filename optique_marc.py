#!/usr/bin/python3

graphe = {'node1': {'node2': 500, 'node3': 600},
            'node2': {'node1': 500, 'node3': 300, 'node4': 400},
            'node3': {'node2': 300, 'node1': 600, 'node5': 400},
            'node4': {'node2': 400, 'node3': 500, 'node5': 300, 'node6': 400},
            'node5': {'node3': 400, 'node4': 300, 'node6': 600},
            'node6': {'node4': 400, 'node5': 600}
            }

def dijkstra(graphe,source,destination,visited=[],distances={},predecessors={}):

    # On vérifie si la source est égale à la destinationination
    if source == destination:
        # Construction du chemin le plus court
        chemin=[]
        pred=destination
        while pred != None:
            chemin.append(pred)
            pred=predecessors.get(pred,None)
        print('Le Plus court chemin entre le noeud1 --> '+destination+' est : ->' +str(chemin[::-1])+" coût="+str(distances[destination]))
    else :    
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[source]=0

        # visite des voisins
        for neighbor in graphe[source] :

            #On vérifie si le noeud voisin a été déjà visité
            if neighbor not in visited:
                nouvelle_distance = distances[source] + graphe[source][neighbor]

                #On
                if nouvelle_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = nouvelle_distance
                    predecessors[neighbor] = source
        
        #On marque la source comme visitée
        visited.append(source)
 
        unvisited={}
        for k in graphe:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))       
        x=min(unvisited, key=unvisited.get)

        #Fonction récurssive
        dijkstra(graphe,x,destination,visited,distances,predecessors)
       


if __name__ == "__main__":
    dijkstra(graphe,'node1','node2',visited=[],distances={},predecessors={});
    dijkstra(graphe,'node1','node3',visited=[],distances={},predecessors={});
    dijkstra(graphe,'node1','node4',visited=[],distances={},predecessors={});
    dijkstra(graphe,'node1','node5',visited=[],distances={},predecessors={});
