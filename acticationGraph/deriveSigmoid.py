import numpy as np
import matplotlib.pyplot as plt

""" 
 하이퍼볼릭 탄젠트 함수
 시그모이드 함수의 대체제로 사용할 수 있는 활성화 함수
"""
class DeriveSigmoid:

    def __init__(self):
        ## x좌표
        self.xCoordinate = np.arange(-10.0, 10.0, 0.1)

    def derivativeSigmoidFunction(self):
        # ==========================================
        #  도함수
        # ==========================================
        tmp1 = list(map(
            lambda x: 1 / (1 + np.exp(-x)),
            self.xCoordinate
        ))

        tmp2 = list(map(
            lambda x:1-x, tmp1
        ))
        yCoordinate = [x*y for x, y in zip(tmp1, tmp2)]
        plt.plot(self.xCoordinate, yCoordinate)

        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")

        # y축 설정
        plt.ylim(-0.1, 0.3)
        plt.show()


def main():
    snode = DeriveSigmoid()
    snode.derivativeSigmoidFunction()


if __name__ == "__main__":
    main()