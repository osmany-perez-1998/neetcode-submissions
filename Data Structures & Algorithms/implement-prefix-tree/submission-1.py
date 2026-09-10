class TrieNode:
    def __init__(self, letter: str):
        self.value = letter
        self.ends_word = False
        self.children = {}


class PrefixTree:
    def __init__(self):
        self.node = TrieNode("")
        

    def insert(self, word: str) -> None:
        aux_node = self.node

        i = 0
        while i < len(word) and word[i] in aux_node.children:
            aux_node = aux_node.children[word[i]]
            i+=1
        for j in range(i, len(word)):
            child_node = TrieNode(word[j])
            aux_node.children[word[j]] = child_node
            aux_node = child_node

        aux_node.ends_word = True



    def search(self, word: str) -> bool:
        aux_node = self.node
        for i in range(len(word)):
            if word[i] in aux_node.children:
                aux_node = aux_node.children[word[i]]
            else:
                return False        
        return aux_node.ends_word


        

    def startsWith(self, prefix: str) -> bool:
        aux_node = self.node
        for i in range(len(prefix)):
            if prefix[i] in aux_node.children:
                aux_node = aux_node.children[prefix[i]]
            else:
                return False
        
        return True
        
        