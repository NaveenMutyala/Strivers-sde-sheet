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




def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None :
            return head
        di = {}
        temp = head
        while temp != None:
            copyNode = Node(temp.val)
            di[temp] = copyNode
            temp = temp.next
        temp = head
        while temp != None:
            di[temp].next = di[temp.next] if temp.next else None
            di[temp].random = di[temp.random] if temp.random else None
            temp = temp.next
        return di[head]
# or
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        while temp != None:
            copyNode = Node(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = temp.next.next
        temp = head
        while temp != None:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next
        dummy = Node(-1)
        res = dummy
        temp = head
        while temp!= None:
            dummy.next = temp.next
            temp.next = temp.next.next
            dummy = dummy.next
            temp = temp.next
        return res.next


def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        for i in range(len(nums)):
            # sm = nums[i]
            # temp = [nums[i]]
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l= i+1
            r = len(nums)-1
            while l<r:
                # tempsms
                sm=nums[l]+nums[r]+nums[i]
                if sm==0:
                    # temp
                    res.append([nums[i],nums[l],nums[r]])
                    # break
                    l+=1
                    r-=1
                    while r>0 and nums[r]==nums[r+1]:
                        r-=1
                    while l<len(nums)-1 and nums[l]==nums[l-1]:
                        l+=1

                elif sm<0:
                    l+=1
                else:
                    r-=1
        return res

def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        leftMax,rightMax = height[l],height[r]
        while l<r:
            if leftMax <rightMax:
                l+=1
                leftMax = max(leftMax,height[l])
                res+=leftMax- height[l]
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                res+=rightMax-height[r]
        return res

def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx=0
        c =0
        for i in nums:
            if i ==1:
                c+=1
            else:
                mx=max(mx,c)
                c=0
        return max(mx,c)

