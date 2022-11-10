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

    def computePerceptronValue(self,row:list) -> float:
        a = 0
        for i in range(self.inputRowLength):
            a += row[i]*row[self.inputRowLength+i]
        return a

    def determineY(self, a:float) -> int:
        return 1 if a>=self.threshold else 0

    def adjustWeight(self, row:list) -> list:
        output = []
        for i in range(self.inputRowLength):
            output.append(row[self.inputRowLength+i]+(self.learning_rate*i))
        return output

    def debugprint(self):
        print(self.learning_rate)
        print(self.threshold)
        print(self.bias)
        print(self.matrix)

    def compute(self):
        indexA = self.inputRowLength*2
        indexY = indexA+1
        indexZ = indexY+1
        print(self.matrix)
        for indexRow in range(len(self.matrix)):
            row = self.matrix[indexRow]
            print(self.computePerceptronValue(row))
            row[indexA] = self.computePerceptronValue(row)
            row[indexY] = self.determineY(row[indexA])
            if(indexRow != len(self.matrix)-1):
                self.matrix[indexRow+1][3:5] = self.adjustWeight(row)

        print(self.matrix)


p = Perceptron()
p.readInput()
p.compute()