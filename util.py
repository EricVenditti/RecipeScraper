import statistics

def remove_outliers(arr):
    avg = statistics.mean(arr)
    std_dev = statistics.stdev(arr)
    for a in arr:
        if (a > avg + std_dev or a < avg - std_dev):
            arr.remove(a)
            avg = statistics.mean(arr)
            std_dev = statistics.stdev(arr)
    return arr
