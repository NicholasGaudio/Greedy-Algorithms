from collections import deque

def OPTFF(k, m, rows, nextRequest):
    cache = {}
    misses = 0

    for i in range(0, len(rows[1])):
        request = int(rows[1][i])
        #print(f"Working on Request: {request}")
        #print(cache)
        if (request in cache):
            #print("Cache Hit")
            cache[request] = i
        else:
            #print("Cache Miss")
            misses += 1
            if len(cache) >= k:
                upNext = -1
                nKey = 0
                for key in cache:
                    if not nextRequest[f"{key}"]:
                        nKey = key
                        break
                    if nextRequest[f"{key}"][0] > upNext:
                        upNext = nextRequest[f"{key}"][0]
                        nKey = key
                del cache[nKey]
            cache[request] = i
        nextRequest[f"{request}"].popleft()
        #print(nextRequest)
        #print(cache)
    print(f"OPTFF : {misses}")