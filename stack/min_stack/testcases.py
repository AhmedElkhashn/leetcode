
import json
import os
from solution import MinStack

minStack = MinStack()

minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top()    == 0
assert minStack.getMin() == -2


print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
