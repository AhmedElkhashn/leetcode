
import json
import os
from solution import Solution, ListNode

s = Solution()

def make_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


head = make_list([1,2,3,4])
s.reorderList(head)
assert list_to_array(head) == [1,4,2,3]

head = make_list([1,2,3,4,5])
s.reorderList(head)
assert list_to_array(head) == [1,5,2,4,3]



print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
