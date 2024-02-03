class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

    def maxMeetings(self, s: List[int], e: List[int], n: int) -> None:
        meet = [meeting(s[i], e[i], i + 1) for i in range(n)]
        sorted(meet, key=lambda x: (x.end, x.pos))
        answer = []
        limit = meet[0].end
        answer.append(meet[0].pos)
        for i in range(1, n):
            if meet[i].start > limit:
                limit = meet[i].end
                answer.append(meet[i].pos)
        print("The order in which the meetings will be performed is ")
        for i in answer:
            print(i, end=" ")
          # or 

def maximumMeetings(self,n,start,end):
        # code here
        newList = []
        for i in range(n):
            newList.append([start[i],end[i]])
        newList.sort(key=lambda x:x[-1])
        res = 1
        currentEnd = newList[0][-1]
        for i in range(1,n):
            if currentEnd<newList[i][0]:
                res+=1
                currentEnd = newList[i][-1]
        return res


def countPlatforms(arr, dep):
    arr.sort()
    dep.sort()


    ans = 1
    count = 1
    i = 1
    j = 0
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:  # one more platform needed
            count += 1
            i += 1
        else:  # one platform can be reduced
            count -= 1
            j += 1
        ans = max(ans, count)  # updating the value with the current maximum
    return ans

def jobScheduling(self, jobs):
        jobs.sort(key=lambda x: x.profit, reverse=True)
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)


        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0


        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobProfit += jobs[i].profit
                    break


        return countJobs, jobProfit
  # or
   def JobScheduling(self,Jobs,n):
        
        # code here
        Jobs.sort(key=lambda x:x.profit,reverse= True)
        res =[False]*(n)
        c= 0
        profit =0
        for i in Jobs:
            j =i.deadline-1
            while j>=0 and res[j]:
                j-=1
            if j>=0:
                res[j]=True
                profit+=i.profit
                # print(i.profit)
                c+=1
        return [c,profit]

  def fractionalKnapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        curWeight = 0
        finalvalue = 0.0
        for i in range(n):
            if curWeight + arr[i].weight <= W:
                curWeight += arr[i].weight
                finalvalue += arr[i].value
            else:
                remain = W - curWeight
                finalvalue += arr[i].value / arr[i].weight * remain
                break
        return finalvalue


# coin change
          V = 49
    ans = []
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = 9
    for i in range(n - 1, -1, -1):
        while V >= coins[i]:
            V -= coins[i]
            ans.append(coins[i])
    print("The minimum number of coins is", len(ans))
    print("The coins are")
    for i in range(len(ans)):
        print(ans[i], end=" ")



