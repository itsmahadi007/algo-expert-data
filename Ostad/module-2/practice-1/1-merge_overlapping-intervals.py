n = int(input())
intervals = []
for i in range(n):
    x = input().split()
    intervals.append((int(x[0]), int(x[1])))

intervals.sort()

merged_intervals = []
for interval in intervals:
    if not merged_intervals or merged_intervals[-1][1] <= interval[0]:
        merged_intervals.append(interval)
    else:
        merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))

for i in merged_intervals:
    print(i[0], i[1])
        
        
        
        



"""
[(1,4), (3,5) ,(7,8)]
"""