# Merge 2 sorted arrays without extra space
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        gap = (n+m)//2 + (n+m)%2
       
        while gap>0:
            left =0
            right = left + gap
            while right< (n+m):
                if nums1[left]>nums1[right]:
                    nums1[left],nums1[right] = nums1[right],nums1[left]
                left+=1
                right+=1
            if gap==1:
                break
            gap = gap//2+gap%2

  # or
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m-1
        r = n-1
        k = m+n-1
        while l>=0 and r>=0:
            if nums1[l]> nums2[r]:
                nums1[k]=nums1[l]
                l-=1
            else:
                nums1[k]= nums2[r]
                r-=1
            k-=1
        while r>=0:
            nums1[k]= nums2[r]
            k-=1
            r-=1
# find duplicates in array
  def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow

# https://www.codingninjas.com/studio/problems/873366?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTabValue=SUBMISSION
def missingAndRepeating(arr, n):
    # Write your code here
    # pass
    sn = (n*(n+1))//2
    s2n = (n*(n+1)*(2*n+1))//6
    s =0
    s2=0
    for i in arr:
        s+=i
        s2+=i*i

    # print(s,s2,sn,s2n)
    val1 = s-sn
    val2 = s2-s2n
    val2 = val2//val1
    x = (val1+val2)//2
    y= val2 - x
    return (y,x)

