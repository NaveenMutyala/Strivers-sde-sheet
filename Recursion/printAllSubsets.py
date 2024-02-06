a =[1,2,3]
temp = []
def subsets(ind):
    print(temp)
    for i in range(ind,len(a)):
        temp.append(a[i])
        subsets(i+1)
        temp.pop()
subsets(0)
