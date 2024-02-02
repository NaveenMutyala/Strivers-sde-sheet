def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        n = 1
        temp = head
        while temp.next!=None:
            n+=1
            temp = temp.next
        temp.next = head
        k = k%n
        end = n-k
        while end !=0:
            end-=1
            temp = temp.next
        head = temp.next
        temp.next = None
        return head


