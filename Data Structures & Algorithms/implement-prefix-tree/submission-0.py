class Node:
    def __init__(self):
        self.children = {}
        self.word = False


class PrefixTree:

    root: Nonde

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.word = True


    def search(self, word: str) -> bool:
        node = self._get(word)
        return node.word if node else False
        

    def startsWith(self, prefix: str) -> bool:
        node = self._get(prefix)
        return True if node else False


    def _get(self, word: str) -> Node:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return None
        return node
        
        