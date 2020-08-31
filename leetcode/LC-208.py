# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(key=None)



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.head

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node(key=ch)
            cur = cur.children[ch]
        cur.data = word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.head

        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return False
        if cur.data != None:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.head

        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
