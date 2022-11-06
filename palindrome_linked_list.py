#linked list 개념 복습 겸, list로 풀어보는 palindrome
#Node /w data, next(reference)

from typing import List

class ListNode():
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = None

## 첫 번째 방법
# def isPalindrome(head: ListNode) -> bool:
#     q: List = []

#     if not head:
#         return True

#     node = head
#     while node:
#         q.append(node.data)
#         node = node.next

#     while len(q) > 1:
#         if q.pop(0) != q.pop():
#             return False

#     return True


## 두 번째 방법 (runner)
def isPalindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    #중앙값이 존재할 경우, palindrome에서 제외
    if fast:
        slow = slow.next
    
    while rev and rev.data == slow.data:
        slow, rev = slow.next, rev.next
    
    return not rev



list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(2)
list4 = ListNode(1)
head = list1
list1.next = list2
list2.next = list3
list3.next = list4

print(isPalindrome(head))