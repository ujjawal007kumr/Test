from typing import Optional

class Node:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        if node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)
        elif node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            return self.right_child.insert(node)
        else:
            return False  # Overlapping intervals

class Calendar:
    def __init__(self):
        self.root: Optional[Node] = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start=start, end=end)
            return True
        return self._insert(node=Node(start, end), current=self.root)

    def _insert(self, node: Node, current: Node) -> bool:
        if current.insert(node):
            return True
        elif node.end <= current.start and current.left_child:
            return self._insert(node, current.left_child)
        elif node.start >= current.end and current.right_child:
            return self._insert(node, current.right_child)
        else:
            return False

calendar = Calendar()
print(calendar.book(5, 10))
print(calendar.book(8, 13))
print(calendar.book(10, 15))
