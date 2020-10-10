graph = {"a": ['b', 'c'],
         "b": ['c'],
         'c': ['d', 'e']
         }

for node in graph:
    print(graph[node])

def bds(graph, node):
    print(node)
    for no in graph[node]:
        bds(graph, no)

bds(graph, 'a')
