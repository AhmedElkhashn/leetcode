
import json
import os
from solution import Solution

s = Solution()

assert s.longestConsecutive([100,4,200,1,3,2]) == 4
assert s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
assert s.longestConsecutive([1,0,1,2]) == 3


print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
