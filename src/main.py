from Functions.FIFO import FIFO
from Functions.LRU import LRU
from Functions.Input import InputHandling

def main():
    input = "Data/in.txt"
    k, m, rows = InputHandling(input)
    FIFO(k, m, rows)
    LRU(k, m, rows)

    Q1 = False

    if Q1:
        print("Q1: FIFO")

if __name__ == "__main__":
    main()