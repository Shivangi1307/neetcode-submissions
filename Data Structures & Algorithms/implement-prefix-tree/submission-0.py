class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()

            current = current.children[ch]

        current.isEnd = True

    def search(self, word: str) -> bool:

        current = self.root

        for ch in word:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return current.isEnd
        

    def startsWith(self, prefix: str) -> bool:

        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return True
        
        