#Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
#Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
#написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
#розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
#написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def insertion_sort(self):
        sorted_head = None
        cur = self.head
        while cur:
            nxt = cur.next
            if sorted_head is None or cur.data < sorted_head.data:
                cur.next = sorted_head
                sorted_head = cur
            else:
                s = sorted_head
                while s.next and s.next.data < cur.data:
                    s = s.next
                cur.next = s.next
                s.next = cur
            cur = nxt
        self.head = sorted_head


def merge_sorted(list1: LinkedList, list2: LinkedList) -> LinkedList:
    result = LinkedList()
    dummy = Node()
    tail = dummy
    a, b = list1.head, list2.head
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b
    result.head = dummy.next
    return result


llist = LinkedList()

llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список:")
llist.print_list()

llist.delete_node(10)
print("\nПісля видалення вузла 10:")
llist.print_list()

print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

llist.reverse()
print("\nПісля реверсування:")
llist.print_list()

llist.insertion_sort()
print("\nПісля сортування:")
llist.print_list()

other = LinkedList()
for x in (30, 12, 2):
    other.insert_at_beginning(x)
other.insertion_sort()

merged = merge_sorted(llist, other)
print("\nОб'єднаний відсортований список:")
merged.print_list()