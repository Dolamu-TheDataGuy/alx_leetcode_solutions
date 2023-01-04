#!/usr/bin/python3
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        temp = head
        while True:
          if list1 is None:
            temp.next = list2
            break
    
          if list2 is None:
            temp.next = list1
            break

          if (list1.val <= list2.val):
            temp.next = list1
            list1 = list1.next
          else:
            temp.next = list2
            list2 = list2.next
          temp = temp.next
        return head.next

if ("__name__" == "__main__"):
    head1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    head1.next = node2
    node2.next = node3

    head2 = ListNode(1)
    node_a = ListNode(3)
    node_b = ListNode(5)
    head2.next = node_a
    node_a.next = node_b

    sol = Solution()
