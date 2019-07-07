import numpy as np
import matplotlib.pyplot as plt

class Step:

    def __init__(self):

        ## x좌표
        self.xCoordinate = np.arange(-5, 5, 0.1)

    def stepFunc(self):

        ## y좌표
        yCoordinate = list(map(
            lambda x: np.array(x > 0, dtype=np.int), self.xCoordinate
        ))

        plt.plot(self.xCoordinate, yCoordinate)
        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")

        plt.show()

def main():
    snode = Step()
    snode.stepFunc()

if __name__ == "__main__":
    main()