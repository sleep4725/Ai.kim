import numpy as np
import matplotlib.pyplot as plt

""" 
 하이퍼볼릭 탄젠트 함수
 시그모이드 함수의 대체제로 사용할 수 있는 활성화 함수
"""
class HyperBolicTangent:

    def __init__(self):
        ## x좌표
        self.xCoordinate = np.arange(-10.0, 10.0, 0.1)

    def tanhGraph(self):
        yCoordinate = list(map(
            lambda x: (1-np.exp(-x))/(1+np.exp(-x)),
            self.xCoordinate
        ))

        plt.plot(self.xCoordinate, yCoordinate)

        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")

        # y축 설정
        plt.ylim(-1.0, 1.0)
        plt.show()


def main():
    snode = HyperBolicTangent()
    snode.tanhGraph()


if __name__ == "__main__":
    main()