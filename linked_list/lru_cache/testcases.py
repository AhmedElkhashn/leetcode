
import json
import os
from solution import LRUCache

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
assert lRUCache.get(1)  == 1
lRUCache.put(3, 3)
assert lRUCache.get(2)  == -1
lRUCache.put(4, 4)
assert lRUCache.get(1)  == -1
assert lRUCache.get(3)  == 3
assert lRUCache.get(4)  == 4



print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
