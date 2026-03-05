from collections import deque

def FIFO(k, m, rows):

    FIFO = deque()
    misses = 0

    for i in range(0, len(rows[1])):
        request = int(rows[1][i])
        #print(f"Working on Request: {request}")
        if request in FIFO:
            #print("Cache Hit")
            pass
        else:
            #print("Cache Miss")
            misses += 1
            if len(FIFO) < k:
                FIFO.append(request)
            else:
                #print (f"Removing {FIFO.popleft()} from FIFO")
                FIFO.popleft()
                FIFO.append(request)
    
    print(f"FIFO Misses: {misses}")
    #print(f"FIFO current size: {len(FIFO)}")
    #print(f"FIFO capacity: {k}")


