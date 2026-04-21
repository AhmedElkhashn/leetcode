
import json
import os
from solution import Solution, ListNode

def make_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


s = Solution()

assert s.hasCycle(make_list_with_cycle([3,2,0,-4], 1)) == True
assert s.hasCycle(make_list_with_cycle([1,2], 0)) == True
assert s.hasCycle(make_list_with_cycle([1], -1)) == False




print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
