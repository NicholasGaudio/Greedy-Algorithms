import random
from pathlib import Path

def fileGen(filename, k, m, maxID):
    with open(filename, "w") as f:
        f.write(f"{k} {m}\n")

        requests = [str(random.randint(1, maxID)) for _ in range(m)]
        f.write(" ".join(requests))

def outputGen(Lm, Fm, Om):
    filepath = Path(__file__).parent.parent.parent
    with open(filepath / "Data/Output/example.out", "w") as f:
        f.write(f"FIFO  : {Fm}\n")
        f.write(f"LRU   : {Lm}\n")
        f.write(f"OPTFF : {Om}\n")

