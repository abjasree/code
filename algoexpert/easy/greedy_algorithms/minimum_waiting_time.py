def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    min_wait_time = 0
    total_queries = len(queries)
    for idx, time in enumerate(queries):
        queries_left = total_queries - (idx + 1)
        min_wait_time += queries_left * time

    return min_wait_time
