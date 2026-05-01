# Node class for double linked list
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None




class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # hashset so look up is O(1)


        # dummy notes to point to LRU & MRU
        self.left = Node(0,0)
        self.right = Node(0,0)


        # connecting nodes
        self.left.next = self.right
        self.right.prev = self.left
       
    def remove(self, node : Node) -> None:


        # get prev & next node
        prev = node.prev
        next = node.next


        # set the next and prev of the nodes surroenind the node to be removed to bypass it
        prev.next = next
        next.prev = prev


    def insert(self, node : Node) -> None: #inserts to the right of the list
       
        # get prev & next node
        next = self.right
        prev = next.prev


        # add the prev and next links to the node
        node.prev = prev
        node.next = next


        # update prev and next to link to the new node
        prev.next = node
        next.prev = node


    def get(self, key: int) -> int:


        if key in self.cache: # check if the key exists


            node = self.cache[key]
            self.remove(node)      # remove & add again to update MRU
            self.insert(node)
            return node.val
       
        return -1
       


    def put(self, key: int, value: int) -> None:


        if key in self.cache:


            self.remove(self.cache[key])  # if key value already exists remove it


        node = Node(key, value)
        self.cache[key] = node  # add node to hashset
        self.insert(node) # add node to list


        if len(self.cache) > self.capacity: # check if capacity is exceeded


            lru = self.left.next
            self.remove(lru)          # remove LRU
            del self.cache[lru.key]
