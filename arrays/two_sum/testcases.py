
import json
import os
from solution import Solution

s = Solution()

assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert s.twoSum([3, 2, 4], 6)      == [1, 2]
assert s.twoSum([3, 3], 6)         == [0, 1]


print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
