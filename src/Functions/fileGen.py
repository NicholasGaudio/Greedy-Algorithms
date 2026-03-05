import random

def fileGen(filename, k, m, maxID):
    with open(filename, "w") as f:
        f.write(f"{k} {m}\n")

        requests = [str(random.randint(1, maxID)) for _ in range(m)]
        f.write(" ".join(requests))
