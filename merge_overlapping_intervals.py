def mergeOverlappingIntervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    output = [intervals[0]]

    for interval in intervals:
        current_start, current_end = interval
        last_interval = output[-1]
        last_start, last_end = last_interval

        if current_start <= last_end:
            last_interval[1] = max(current_end, last_end)
        else:
            output.append(interval)

    return output
