
import json
import os
from solution import Solution, Node

def make_list(values):
    if not values:
        return None
    nodes = [Node(v) for v, _ in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, random_index) in enumerate(values):
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0]

def list_to_array(head):
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    result = []
    for node in nodes:
        random_index = nodes.index(node.random) if node.random else None
        result.append([node.val, random_index])
    return result

s = Solution()

head = make_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
assert list_to_array(s.copyRandomList(head)) == [[7,None],[13,0],[11,4],[10,2],[1,0]]

head = make_list([[1,1],[2,1]])
assert list_to_array(s.copyRandomList(head)) == [[1,1],[2,1]]

head = make_list([[3,None],[3,0],[3,None]])
assert list_to_array(s.copyRandomList(head)) == [[3,None],[3,0],[3,None]]

print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
