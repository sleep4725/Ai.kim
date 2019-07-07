import numpy as np
import matplotlib.pyplot as plt


class SigmoidGraph:

    def __init__(self):
        ## x좌표
        self.xCoordinate = np.arange(-10, 10, 0.1)

    def sigGraph(self):
        ## y좌표
        yCoordinate = list(map(
            lambda x: 1/(1+np.exp(-x)), self.xCoordinate
        ))

        plt.plot(self.xCoordinate, yCoordinate)
        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")

        plt.show()


def main():
    snode = SigmoidGraph()
    snode.sigGraph()


if __name__ == "__main__":
    main()