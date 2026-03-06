from Functions.FIFO import FIFO
from Functions.LRU import LRU
from Functions.OPTFF import OPTFF
from Functions.Input import InputHandling
from Functions.fileGen import fileGen, outputGen

def main():
    input = "Data/example.in"
    k, m, rows, nextRequest = InputHandling(input)
    Fm = FIFO(k, m, rows)
    Lm = LRU(k, m, rows)
    Om = OPTFF(k, m, rows, nextRequest)

    outputGen(Lm, Fm, Om)

    Q1 = False

    if Q1:
        fileGen("Data/Q1-Files/in1.txt", 5, 50, 7)
        fileGen("Data/Q1-Files/in2.txt", 8, 60, 10)
        fileGen("Data/Q1-Files/in3.txt", 10, 70, 15)

        print("=====File 1=====")
        k, m, rows, nextRequest = InputHandling("Data/Q1-Files/in1.txt")
        FIFO(k, m, rows)
        LRU(k, m, rows)
        OPTFF(k, m, rows, nextRequest)
        print("\n")
        print("=====File 2=====")
        k, m, rows, nextRequest = InputHandling("Data/Q1-Files/in2.txt")
        FIFO(k, m, rows)
        LRU(k, m, rows)
        OPTFF(k, m, rows, nextRequest)
        print("\n")
        print("=====File 3=====")
        k, m, rows, nextRequest = InputHandling("Data/Q1-Files/in3.txt")
        FIFO(k, m, rows)
        LRU(k, m, rows)
        OPTFF(k, m, rows, nextRequest)
        

if __name__ == "__main__":
    main()