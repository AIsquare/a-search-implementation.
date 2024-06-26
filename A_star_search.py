tree = {'S': [['A', 1], ['B', 5], ['C', 8]],
        'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
        'B': [['S', 5], ['G', 4]],
        'C': [['S', 8], ['G', 5]],
        'D': [['A', 3]],
        'E': [['A', 7]]}

tree2 = {'S': [['A', 1], ['B', 2]],
         'A': [['S', 1]],
         'B': [['S', 2], ['C', 3], ['D', 4]],
         'C': [['B', 2], ['E', 5], ['F', 6]],
         'D': [['B', 4], ['G', 7]],
         'E': [['C', 5]],
         'F': [['C', 6]]
         }
heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0}
heuristic2 = {'S': 0, 'A': 5000, 'B': 2, 'C': 3, 'D': 4, 'E': 5000, 'F': 5000, 'G': 0}

cost = {'S': 0}             # total cost for nodes visited


def AStarSearch():

        global tree, heuristic
        closed = []             # closed nodes
        opened = [['S', 8]]     # starting node 'S' with a heuristic value of 8
#This indicates that the estimated total cost from the starting node to the goal node, passing through this node, is 8.
        while True:
                #print(closed)
                fn = [i[1] for i in opened] #f(n) = g(n) + h(n)
                #print('f()',fn)
                chosen_index = fn.index(min(fn)) # min heuristic cost index of a node
                #print('chosen_index',chosen_index)
                node = opened[chosen_index][0] # Give me the node of min heuristic index of node
                #print(node)
                closed.append(opened[chosen_index])
                del opened[chosen_index] #Once explored remove
                if closed[-1][0] == 'G':
                        break
                for item in tree[node]:
                        #print(item)
                        if item[0] in [closed_item[0] for closed_item in closed]:
                                continue
                        #print(node,cost[node])
                        cost.update({item[0]: cost[node] + item[1]}) # cost to reach the node
                        #print(cost)
                        fn_node = cost[node] + heuristic[item[0]] + item[1]     # Total, calculate f(n) of current node
                        #print(fn_node)
                        temp = [item[0], fn_node]
                        opened.append(temp)      # store f(n) of current node in array opened      
        '''Optimal sequence'''

        trace_node = 'G'
        optimal_sequence = ['G']
        #print(closed)
        for i in range(len(closed)-2,-1,-1):
                #print(closed[i])

                check_node = closed[i][0]
                print('check_node',check_node)
                #print([children for children in tree[check_node]])
                if trace_node in [children[0] for children in tree[check_node]]:
                        children_costs = [temp[1] for temp in tree[check_node]]
                        children_nodes = [temp[0] for temp in tree[check_node]]
                        #print(children_costs,children_nodes)
                        ''' check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence
                                change the correct optimal tracing node to current node'''
                        if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                                optimal_sequence.append(check_node)
                                trace_node = check_node
        optimal_sequence.reverse()
        return closed, optimal_sequence

if __name__ == '__main__':
    visited_nodes, optimal_nodes = AStarSearch()
    print('visited nodes: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))
