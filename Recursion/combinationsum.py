
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.h=[]
        self.picking(0,candidates,[],target)
        return self.h
    def picking(self,i,arr,a,target):
        if i==len(arr):
            if target==0:
                self.h.append(a[:])
            return 
        if arr[i]<=target:
            a.append(arr[i])
            self.picking(i,arr,a,target-arr[i])
            a.pop()
        self.picking(i+1,arr,a,target)
        
