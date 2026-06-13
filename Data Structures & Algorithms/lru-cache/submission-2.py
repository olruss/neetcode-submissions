class Node:
    key: int
    val: int
    prev: "Node" | None
    next: "Node" | None

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    start: Node
    end: Node
    cap: int
    cache: dict[int, Node]


    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.start = Node(0, 0)
        self.end = Node(0, 0)
        self.start.next = self.end
        self.end.prev = self.start
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._touch(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.cap and key not in self.cache:
            # pop one key if cap is exceeded
            node = self.start.next
            self.start.next = node.next
            node.next.prev = self.start
            self.cache.pop(node.key)
        # key exist -> update
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._touch(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            node.next = self.end
            node.prev = self.end.prev
            self.end.prev.next = node
            self.end.prev = node

    def _touch(self, node):
        # pop node
        _prev, _next = node.prev, node.next
        _prev.next = _next
        _next.prev = _prev
        # and put to end
        node.next = self.end
        node.prev = self.end.prev
        self.end.prev.next = node
        self.end.prev = node

        
