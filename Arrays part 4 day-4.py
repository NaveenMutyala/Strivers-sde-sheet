def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        res=[]
        for i in range(len(nums)):
            di[nums[i]] =i
        for i in range(len(nums)):
            if target-nums[i] in di and di[target-nums[i]] != i:
                # return [i,di[(target-di[i])]]
                res.append(i)
                res.append(di[(target-nums[i])])
                return res


 def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                hashset = set()
                for k in range(j+1,len(nums)):
                    sum_ = nums[i]+nums[j]+nums[k]
                    fourth = target - sum_
                    if fourth in hashset:
                        # res.append([nums])
                        temp = [nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        res.add(tuple(temp))
                    hashset.add(nums[k])
        ans = [list(t) for t in res]
        return ans

# O(n^3 *log(n))

def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        # print(n)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k = j+1
                l = n-1
                while k<l:
                    sum_ = nums[i]+ nums[j]+ nums[k]+nums[l]
                    # print(sum_)
                    if target == sum_:
                        temp =[nums[i],nums[j],nums[k],nums[l]]
                        # print(temp)
                        res.append(temp)
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]== nums[l+1]:
                            l-=1
                    elif target > sum_ :
                        k+=1
                    else:
                        l-=1
        return res
        # O(n^3)


def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        cnt =0
        longest = 1
        lastSmaller = float('-inf')
        for i in range(len(nums)):
            if nums[i] -1 == lastSmaller:
                cnt+=1
                lastSmaller = nums[i]
            elif nums[i]!= lastSmaller:
                cnt =1
                lastSmaller = nums[i]
            longest = max(cnt,longest)
        return longest

def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        st = set()
        for i in nums:
            st.add(i)
        longest = 1
        cnt =0
        for i in st:
            if i-1 not in st:
                cnt = 1
                x = i

                while x+1 in st:
                    cnt+=1
                    x=x+1
                longest = max(cnt,longest)
        return longest

