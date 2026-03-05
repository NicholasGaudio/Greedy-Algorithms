from collections import deque


def FIFO(filepath):
    with open(filepath, 'r') as input:
        lines = input.readlines()

    rows = []
    for line in lines:
        rows.append(line.strip().split())
    try:
        k = int(rows[0][0])
        m = int(rows[0][1])
    except (IndexError, ValueError):
        print("Error: Invalid input format.")
        return
    FIFO = deque()
    misses = 0

    # Input error handling
    if (len(rows) != 2):
        print("Error: Number of requests does not match the number of rows in the input file.")
        return
    if (len(rows[1]) != m):
        print("Error: Number of requests does not match the number of requests specified in the input file.")
        return

    #iterate thorugh the requests on second line and handle FIFO logic
    requests = []
    for i in range(0, len(rows[1])):
        request = int(rows[1][i])
        print(f"Working on Request: {request}")
        if request in FIFO:
            print("Cache Hit")
        else:
            print("Cache Miss")
            misses += 1
            if len(FIFO) < k:
                FIFO.append(request)
            else:
                FIFO.popleft()
                FIFO.append(request)
    
    print(f"FIFO Misses: {misses}")


