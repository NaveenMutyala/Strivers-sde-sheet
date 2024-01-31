def reverseLinkedList(head):
    
    # Initialize 'temp' at the
    # head of the linked list
    temp = head
    
    # Initialize 'prev' to None,
    # representing the previous node 
    prev = None
    
    while temp is not None:
        # Store the next node in 'front'
        # to preserve the reference
        front = temp.next
        # Reverse the direction of the current
        # node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current 
        # node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node
        # advancing traversal
        temp = front

    # Return the new head
    # of the reversed linked list
    return prev

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

 def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val > list2.val :
            list1,list2 = list2,list1
        res = list1
        temp = None
        while list1 is not None and list2 is not None:
            temp = list1
            while list1 is not None and list1.val<=list2.val:
                temp = list1
                list1 = list1.next
            temp.next = list2
            list1,list2= list2,list1
        return res


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        delNode = slow.next
        slow.next = slow.next.next
        delNode = None
        return head


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        temp = dummy
        carry = 0
        while (l1 != None or l2 != None) or carry:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            node = ListNode(sum % 10)
            temp.next = node
            temp = temp.next
        return dummy.next

def deleteNode(t: Node) -> None:
    t.num = t.next.num
    t.next = t.next.next
    return
