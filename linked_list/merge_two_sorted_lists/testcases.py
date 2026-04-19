import json
import os
from solution import Solution, ListNode

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

s = Solution()

assert list_to_array(s.mergeTwoLists(make_list([1,2,4]),make_list([1,3,4]))) == [1,1,2,3,4,4]
assert list_to_array(s.mergeTwoLists(make_list([]),make_list([]))) == []
assert list_to_array(s.mergeTwoLists(make_list([]),make_list([0]))) == [0]

print("All tests passed!")

# Mark as solved in problem.json
json_path = os.path.join(os.path.dirname(__file__), "problem.json")

with open(json_path, "r") as f:
    data = json.load(f)

data["solved"] = True

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

print("problem.json updated — status: solved")
