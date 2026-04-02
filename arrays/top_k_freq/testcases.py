
import json
import os
from solution import Solution

s = Solution()

assert s.topKFrequent([1,1,1,2,2,3],2) == [1,2]
assert s.topKFrequent([1],1) == [1]
assert s.topKFrequent([1,2,1,2,1,2,3,1,3,2],2) == [1,2]


print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
