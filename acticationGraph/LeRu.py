import numpy as np
import matplotlib.pyplot as plt


class LeRuGraph:

    def __init__(self):
        ## x좌표
        self.xCoordinate = np.arange(-10.0, 10.0, 0.1)

    def reLu(self):
        yCoordinate = list(map(
            lambda x: np.maximum(0, x),
            self.xCoordinate
        ))

        plt.plot(self.xCoordinate, yCoordinate)

        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")

        # y축 설정
        plt.ylim(-1.0, 7.0)
        plt.show()

    def leakyReLu(self):
        yCoordinate = list(map(
            lambda x: np.maximum(0.01*x, x),
            self.xCoordinate
        ))

        plt.plot(self.xCoordinate, yCoordinate)

        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")

        # y축 설정
        plt.ylim(-1.0, 7.0)
        plt.show()

    def elu(self):
        yCoordinate = list()

        for i in self.xCoordinate:
            if i < 0: yCoordinate.append(np.exp(i)-1)
            else:     yCoordinate.append(i)

        plt.plot(self.xCoordinate, yCoordinate)

        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")

        # y축 설정
        plt.ylim(-1.0, 7.0)
        plt.show()

def main():
    snode = LeRuGraph()
    snode.elu()
    #snode.leakyReLu()
    #snode.reLu()


if __name__ == "__main__":
    main()