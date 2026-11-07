#Завдання 3. Дерева, алгоритм Дейкстри
#Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
#Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

import heapq


class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, weight):
        self.adj.setdefault(u, {})[v] = weight
        self.adj.setdefault(v, {})[u] = weight

    def dijkstra(self, start):
        dist = {v: float("inf") for v in self.adj}
        prev = {v: None for v in self.adj}
        dist[start] = 0
        heap = [(0, start)] 

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]: 
                continue
            for v, w in self.adj[u].items():
                new_d = d + w
                if new_d < dist[v]:
                    dist[v] = new_d
                    prev[v] = u
                    heapq.heappush(heap, (new_d, v))

        return dist, prev


def get_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1]


g = Graph()
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 1)
g.add_edge("B", "C", 2)
g.add_edge("B", "D", 1)
g.add_edge("C", "D", 4)
g.add_edge("D", "E", 3)

dist, prev = g.dijkstra("A")
for v in g.adj:
    print(f"A -> {v}: відстань {dist[v]}, шлях {get_path(prev, v)}")