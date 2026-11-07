#Завдання 5. Візуалізація обходу бінарного дерева
#Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
#Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). 
#Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

import uuid
import heapq
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def heap_to_tree(heap, i=0):
    if i >= len(heap):
        return None
    node = Node(heap[i])
    node.left = heap_to_tree(heap, 2 * i + 1)
    node.right = heap_to_tree(heap, 2 * i + 2)
    return node


def gradient_colors(n, start=(10, 40, 90), end=(190, 225, 255)):
    colors = []
    for i in range(n):
        t = i / (n - 1) if n > 1 else 0
        r, g, b = (round(s + (e - s) * t) for s, e in zip(start, end))
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors


def text_color(color):
    if not color.startswith("#"):
        return "black"
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    return "white" if 0.299 * r + 0.587 * g + 0.114 * b < 128 else "black"


def dfs_iterative(root):
    order, stack = [], [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right: 
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def bfs_iterative(root):
    order, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def draw_step(root, title):
    plt.clf()
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [d["color"] for _, d in tree.nodes(data=True)]
    nx.draw(tree, pos=pos, with_labels=False, arrows=False,
            node_size=2500, node_color=colors)
    for node_id, d in tree.nodes(data=True):
        nx.draw_networkx_labels(tree, pos, labels={node_id: d["label"]},
                                font_color=text_color(d["color"]))
    plt.title(title)
    plt.pause(0.8)


def visualize(root, order, title):
    plt.figure(figsize=(8, 5))
    for node, color in zip(order, gradient_colors(len(order))):
        node.color = color
        draw_step(root, title)
    plt.show()


data = [10, 4, 1, 5, 3, 0, 7, 8, 2, 6]
heapq.heapify(data)

root = heap_to_tree(data)
visualize(root, dfs_iterative(root), "Обхід у глибину (DFS, стек)")

root = heap_to_tree(data) 
visualize(root, bfs_iterative(root), "Обхід у ширину (BFS, черга)")