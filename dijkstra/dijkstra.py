import sys
import copy
import heapq

def Dijkstra_using_priority_queue(graph, source, target):
    # 꼭지점 set
    dist = {}
    prev = {}
    Q = []

    for vertex in graph:
        if vertex != source:
            dist[vertex] = sys.maxsize # 소스에서 꼭지점 까지 아직 모르는 길이
        else:
            dist[vertex] = 0           # 소스에서 소스까지
        prev[vertex] = None            # 소스에서 최적 경로의 이전 꼭지점

        heapq.heappush(Q, [dist[vertex], vertex])
        
    while Q:
        min = heapq.heappop(Q)[1] # 가장 높은 우선순위의 꼭지점을 제거하고 반환

        # 인접 꼭지점의 최단 경로 
        for v in graph[min]:
            alt = dist[min] + graph[min][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = min
            
            # decrease proirity
            for t in Q:
                if t[1] == v:
                    t[0] = alt
                    break    
            heapq.heapify(Q)

    # 경로            
    path = []
    u = target
    while prev[u]:
        path.insert(0, u)        
        u = prev[u]
    path.insert(0, u) # 마지막으로 소스를 삽입
    print(path)

def Dijkstra(graph, source, target):
    # 꼭지점 set    
    Q = copy.deepcopy(graph)

    dist = {}
    prev = {}

    for vertex in Q:
        dist[vertex] = sys.maxsize # 소스에서 꼭지점 까지 아직 모르는 길이
        prev[vertex] = None        # 소스에서 최적 경로의 이전 꼭지점

    dist[source] = 0 # 소스에서 소스까지
    
    while Q:
        # 최소 거리를 갖는 꼭지점 선택
        min = sys.maxsize
        for key in Q:
            if dist[key] < min:
                min = dist[key]
                next = key
        u = Q[next]

        # 선택한 꼭지점은 목록에서 제거
        del Q[next]

        # 인접 꼭지점의 최단 경로
        for v in u:
            alt = dist[next] + u[v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = next

    # 경로            
    path = []
    u = target
    while prev[u]:
        path.insert(0, u)        
        u = prev[u]
    path.insert(0, u) # 마지막으로 소스를 삽입
    print(path)

if __name__ == '__main__':
    graph = {}
    graph['a'] = {'b': 4, 'c': 3}
    graph['b'] = {'a': 4, 'c': 2, 'd': 5}
    graph['c'] = {'a': 3, 'b': 2, 'd': 3, 'e': 6}
    graph['d'] = {'b': 5, 'c': 3, 'e': 1, 'f': 5}
    graph['e'] = {'c': 6, 'd': 1, 'g': 5}
    graph['f'] = {'d': 5, 'g': 2, 'z': 7}
    graph['g'] = {'e': 5, 'f': 2, 'z': 4}
    graph['z'] = {'f': 7, 'g': 4}

    Dijkstra(graph, 'a', 'z')

    Dijkstra_using_priority_queue(graph, 'a', 'z')
