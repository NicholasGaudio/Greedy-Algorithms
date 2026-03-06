from Functions.FIFO import FIFO
from Functions.LRU import LRU
from Functions.OPTFF import OPTFF
from Functions.Input import InputHandling
from Functions.fileGen import fileGen

def main():
    input = "Data/in.txt"
    k, m, rows = InputHandling(input)
    FIFO(k, m, rows)
    LRU(k, m, rows)
    OPTFF(k, m, rows)

    Q1 = False

    if Q1:
        fileGen("Data/Q1-Files/in1.txt", 5, 50, 5)
        fileGen("Data/Q1-Files/in2.txt", 8, 60, 10)
        fileGen("Data/Q1-Files/in3.txt", 10, 70, 15)

        print("=====File 1=====")
        k, m, rows = InputHandling("Data/Q1-Files/in1.txt")
        FIFO(k, m, rows)
        LRU(k, m, rows)
        # add OPTFF
        print("\n")
        print("=====File 2=====")
        k, m, rows = InputHandling("Data/Q1-Files/in2.txt")
        FIFO(k, m, rows)
        LRU(k, m, rows)
        # add OPTFF
        print("\n")
        print("=====File 3=====")
        k, m, rows = InputHandling("Data/Q1-Files/in3.txt")
        FIFO(k, m, rows)
        LRU(k, m, rows)
        # add OPTFF
        

if __name__ == "__main__":
    main()