from collections import deque

def InputHandling(filepath):
    with open(filepath, 'r') as input:
        lines = input.readlines()

    """I need a 2D array that contains when the next request for a specific value occurs next"""
    rows = []
    for line in lines:
        
        rows.append(line.strip().split())
    try:
        k = int(rows[0][0])
        m = int(rows[0][1])
    except (IndexError, ValueError):
        print("Error: Invalid input format.")
        return

    # Input error handling
    if (len(rows) != 2):
        print("Error: Number of requests does not match the number of rows in the input file.")
        return
    if (len(rows[1]) != m):
        print("Error: Number of requests does not match the number of requests specified in the input file.")
        return
    
    nextRequest = {}

    step = 0
    for val in rows[1]:
        if not val in nextRequest:
            nextRequest[val] = deque()
        nextRequest[val].append(step)
        step+=1

    return k, m, rows, nextRequest