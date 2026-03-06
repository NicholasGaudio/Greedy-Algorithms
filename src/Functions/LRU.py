def LRU(k, m, rows):

    LRU = {}
    misses = 0

    for i in range(0, len(rows[1])):
        request = int(rows[1][i])
        #print(f"Working on Request: {request}")
        if (request in LRU):
            #print("Cache Hit")
            LRU[request] = i
        else:
            #print("Cache Miss")
            misses += 1
            if len(LRU) < k:
                LRU[request] = i
            else:
                # Find the least recently used request and remove it from the cache
                minimum = min(LRU.values())
                for key in LRU:
                    if LRU[key] == minimum:
                        #print(f"Removing {key} from LRU")
                        del LRU[key]
                        break
                LRU[request] = i

    print(f"LRU   : {misses}")