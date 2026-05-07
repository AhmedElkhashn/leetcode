
import json
import os
from solution import Solution

s = Solution()

assert s.search([-1,0,3,5,9,12],9) == 4
assert s.search([-1,0,3,5,9,12],2) == -1


print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
