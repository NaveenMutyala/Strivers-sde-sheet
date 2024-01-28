
# n//2
def majorityElement(self, nums: List[int]) -> int:
        cnt =0
        el = None
        for i in range(len(nums)):
            if cnt ==0:
                cnt+=1
                el = nums[i]
            elif nums[i]==el:
                cnt+=1
            else:
                cnt-=1
        return el
# n//3
 def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 =0
        cnt2=0
        el1=None
        el2= None

        for i in range(len(nums)):
            if cnt1==0 and el2 != nums[i]:
                cnt1+=1
                el1 = nums[i]
            elif cnt2==0 and el1 != nums[i]:
                cnt2+=1
                el2 = nums[i]
            elif nums[i]==el1:
                cnt1+=1
            elif nums[i]==el2:
                cnt2+=1
            else :
                cnt1-=1
                cnt2-=1
        li = []
        c1 , c2 = 0, 0
        for i in nums:
            if i == el1:
                c1+=1
            elif i==el2:
                c2+=1
        if c1> len(nums)//3:
            li.append(el1)
        if c2>len(nums)//3:
            li.append(el2)
        return li



def uniquePaths(self, m: int, n: int) -> int:
        di ={}
        def paths(i,j,m,n):
            if i==m-1 and j==n-1:
                return 1 
            if (i,j) in di:
                return di[(i,j)]
            left, right = 0,0
            if i+1<m:
               left =  paths(i+1,j,m,n)
            if j+1<n :
               right = paths(i,j+1,m,n)
            di[(i,j)] = right+left
            return right+left
        c = paths(0,0,m,n)
        return c

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = n + m - 2
        r = m - 1
        res = 1
        for i in range(1, r + 1):
            res = res * (N - r + i) / i
        return int(res)
if __name__ == "__main__":
    obj = Solution()
    totalCount = obj.uniquePaths(2, 3)
    print("The total number of Unique Paths are", totalCount)
