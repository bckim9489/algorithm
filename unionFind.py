'''
def dfs_metrix(graph, i, visited):
    stack = [i]
    result = []

    while stack:
        val = stack.pop()
        if not visited[val]:
            visited[val] = True
            result.append(val)
            for j in range(len(graph[val])-1, 0, -1):
                if graph[val][j] != 0:
                    stack.append(j)
    return result

def dfs_list(graph, i, visited):
    stack = [i]
    result = []

    while stack:
        val = stack.pop()
        if not visited[val]:
            visited[val] = True
            result.append(val)
            stack.extend(reversed(graph[val]))
    return result
'''

def bfs_metrix(graph, i, visited):
    queue = deque()
    queue.append(i)
    result = []

    while queue:
        val = queue.popleft()
        if not visited[val]:
            visited[val] = True
            result.append(val)
            for j in range(len(graph[val])):
                if graph[val][j] != 0 and not visited[j]:
                    queue.append(j)
    return result

from collections import deque

def bfs_list(graph, i, visited):
    queue = deque()
    queue.append(i)
    result = []

    while queue:
        val = queue.popleft()
        if not visited[val]:
            visited[val] = True
            result.append(val)
            queue.extend(graph[val])
    return result

if __name__ == "__main__":
    graph_list = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    visited_list = [False] * len(graph_list)
    result_list = bfs_list(graph_list, 1, visited_list)
    print(result_list)   
    
    '''
    result_list = dfs_list(graph_list, 1, visited_list)
    print(result_list)
    '''
    graph_metrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    visited_metrix = [False] * len(graph_metrix[0])

    result_metrix = bfs_metrix(graph_metrix, 1, visited_metrix)
    print(result_metrix)
    '''

    result_metrix = dfs_metrix(graph_metrix, 1, visited_metrix)
    print(result_metrix)
    '''
