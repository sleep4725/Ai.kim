import numpy as np

class Test:

    def __init__(self):
        self.inputLayer  = np.array([[0, 0], [1, 0], [0, 1], [1, 1]]) # 입력층 (4, 2)
        self.weightLayer = np.array([0.5, 0.5])                       # 가중치 (1, 2)

    def tmpFunc(self):
        print ("np.shape(self.inputLayer)  : {}".format(np.shape(self.inputLayer)))
        print ("np.shape(self.weightLayer) : {}".format(np.shape(self.weightLayer)))


    """ AND Gate
    """
    def andGate(self):
        bias = -0.7
        for x1, x2 in self.inputLayer:
            # ====================
            # activate function
            y = np.dot(self.weightLayer.T, np.array([x1, x2])) + bias
            # print (y)
            # ====================

            if y <= 0:
                print ("({}, {}) -> {}".format(x1, x2, 0))
            else:
                print ("({}, {}) -> {}".format(x1, x2, 1))

    """ OR Gate
    """
    def orGate(self):
        bias = -0.2
        for x1, x2 in self.inputLayer:
            # ====================
            # activate function
            y = np.dot(self.weightLayer.T, np.array([x1, x2])) + bias
            # print(y)
            # ====================

            if y <= 0:
                print("({}, {}) -> {}".format(x1, x2, 0))
            else:
                print("({}, {}) -> {}".format(x1, x2, 1))

def main():
    tobj = Test() # 객체 생성
    #tobj.andGate()
    tobj.orGate()

if __name__ == "__main__":
    main()