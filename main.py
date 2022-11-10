class Perceptron:
    def __init__(self):
        self.learning_rate = 0.1
        self.threshold = 0.5
        self.bias = 1
        self.matrix = []
        self.inputRowLength = 0

    def readInput(self):
        with open("input.txt", "r") as inputFile:
            inputList = inputFile.readlines()
            self.learning_rate = float(inputList.pop(0))
            self.threshold = float(inputList.pop(0))
            self.bias = float(inputList.pop(0))

            try:     
                for row in inputList:
                    rowList = [int(x) for x in row.split()]
                    self.inputRowLength = len(rowList)
                    if len(inputList) != 2**(self.inputRowLength-1):
                        raise IndexError
                    rowList[(self.inputRowLength-1):(self.inputRowLength-1)] = [0 for x in range(self.inputRowLength+2)]
                    self.matrix.append(rowList)
            except IndexError as e:
                print("Error: Invalid self.matrix")

    def computePerceptronValue(row:list):
        
        pass

    def determineY():
        pass

    def adjustWeight():
        pass

    def debugprint(self):
        print(self.learning_rate)
        print(self.threshold)
        print(self.bias)
        print(self.matrix)

    def compute(self):
        indexA = self.inputRowLength*2
        indexY = indexA+1
        indexZ = indexY+1
        for row in self.matrix:
            row[indexA] = self.computePerceptronValue(row)


p = Perceptron()
p.readInput()
