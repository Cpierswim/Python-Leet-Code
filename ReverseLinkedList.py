# Leetcode #206

#Definition for singly-linked list. Provided by Leetcode in order to be able to complete solution
class ListNode:    
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last = None

    def push(self, val) -> None:
        node = ListNode(val)
        if(self.head is None):
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def convertToArray(self):
        arr = []
        workingNode = self.head
        while(workingNode):
            arr.append(workingNode.val)
            workingNode = workingNode.next

        return arr
            

class Solution:
    def reverseList(self, head) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    

#Create a list
list = LinkedList()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)



print(list.convertToArray()) # Should be [1, 2, 3, 4, 5]

print(type(list.head))
test = Solution()
test.reverseList(list.head)

print(list.convertToArray()) # Should be [5, 4, 3, 2, 1], I must have something setup wrong here because it works on Leetcode but not here