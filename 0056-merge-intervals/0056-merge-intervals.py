class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        # Built-in sort without lambda defaults to comparing elements sequentially 
        # (effectively sorting by start time first)
        intervals.sort()
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            # If current start <= last merged end, they overlap
            if current[0] <= merged[-1][1]:
                # Merge by updating the end boundary if the current end is larger
                if current[1] > merged[-1][1]:
                    merged[-1][1] = current[1]
            else:
                # No overlap, append the non-overlapping interval
                merged.append(current)
                
        return merged