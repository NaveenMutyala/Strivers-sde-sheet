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

          
