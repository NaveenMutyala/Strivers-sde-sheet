def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        temp=[]
        def subsets(ind):
            output.append(temp[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                subsets(i+1)
                temp.pop()
        nums.sort()
        subsets(0)
        return output
