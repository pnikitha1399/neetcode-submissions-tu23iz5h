class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        res = [intervals[0]]
        for s, e in intervals:
            le = res[-1][1]
            if s<=le:
                res[-1][1]=max(le,e)
            else:
                res.append([s,e])
        return res