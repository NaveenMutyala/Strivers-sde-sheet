def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA,headB
        while a!=b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow :
                return True
        return False


def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevnode = None
        def kthNode(temp,k):
            k-=1
            while temp!= None and k>0:
                k-=1
                temp = temp.next
            return temp
        def reverse(head):
            temp = head
            prev = None
            while temp is not None:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            return prev



        while temp != None :
            knode = kthNode(temp,k)
            if knode is None:
                if prevnode != None:
                    prevnode.next = temp
                break
            nextnode = knode.next
            knode.next = None
            reverse(temp)

            if head == temp:
                head = knode
            else:
                prevnode.next = knode
            prevnode = temp
            temp = nextnode
        return head


def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # stk =[]
        if head is None or head.next is None:
            return True
        fast = head
        slow = head
        while fast.next != None and fast.next.next!= None:
            fast = fast.next.next
            # stk.append(slow.val)
            slow = slow.next
        slow.next = self.reverse(slow.next)
        slow = slow.next
        temp = head
        while slow!= None:
            if slow.val != temp.val:
                return False
            slow = slow.next
            temp = temp.next
              
        return True
    def reverse(self,ptr):
        pre = None
        next = None
        while ptr != None:
            next = ptr.next
            ptr.next = pre

            pre = ptr
            ptr = next
        return pre  



def CycleNode(head):
    # Write your code here
    # pass
    fast, slow = head, head
    while fast != None and fast.next != None:
    
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
    return None



