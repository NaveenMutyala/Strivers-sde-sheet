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
  
