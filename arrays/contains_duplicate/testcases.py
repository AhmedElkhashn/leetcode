
import json
import os
from solution import Solution


s = Solution()

assert s.containsDuplicate([1, 2, 3, 1]) == True
 
assert s.containsDuplicate([1, 2, 3, 4]) == False

assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

print("All tests passed!")

json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — solved: true")