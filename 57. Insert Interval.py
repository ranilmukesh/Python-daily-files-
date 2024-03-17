class Solution(object):
    def insert(self, intervals, newInterval):

        n,i=len(intervals),0
        res=[]

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        
        while i<n and newInterval[1] >= intervals[i][0]:
            newInterval[0]=min(intervals[i][0],newInterval[0])
            newInterval[1]=max(intervals[i][1],newInterval[1])
            i+=1
        res.append(newInterval)

        while i<n :
            res.append(intervals[i])
            i+=1
        
        return res
