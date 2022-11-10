class Perceptron:
    def __init__(self):
        self.learning_rate = 0.1
        self.threshold = 0.5
        self.bias = 1
        self.matrix = []
        self.inputRowLength = 0
        self.indexA = 0
        self.indexY = 0
        self.indexZ = 0

    def readInput(self):
        with open("input.txt", "r") as inputFile:
            inputList = inputFile.readlines()
            self.learning_rate = float(inputList.pop(0))
            self.threshold = float(inputList.pop(0))
            self.bias = float(inputList.pop(0))
            print(self.bias)

            try:     
                for row in inputList:
                    rowList = [float(x) for x in row.split()]
                    self.inputRowLength = len(rowList)
                    if len(inputList) != 2**(self.inputRowLength-1):
                        raise IndexError
                    # add the b in matrix
                    rowList[(self.inputRowLength-1):(self.inputRowLength-1)] = [self.bias]
                    # add the w0 ... wb columns and also the a and y columns
                    rowList[(self.inputRowLength):(self.inputRowLength)] = [0.0 for x in range(self.inputRowLength+2)]
                    self.matrix.append(rowList)
            except IndexError as e:
                print("Error: Invalid self.matrix")
            
            self.indexA = self.inputRowLength*2
            self.indexY = self.indexA+1
            self.indexZ = self.indexY+1

    def computePerceptronValue(self,row:list) -> float:
        a = 0
        for i in range(self.inputRowLength):
            a += row[i]*row[self.inputRowLength+i]
        return a

    def determineY(self, a:float) -> float:
        return 1.0 if a>=self.threshold else 0.0

    def adjustWeight(self, row:list) -> list:
        output = []
        for i in range(self.inputRowLength):
            output.append(row[self.inputRowLength+i]+(self.learning_rate*row[i]*(row[self.indexZ]-row[self.indexY])))
        return output

    def debugprint(self):
        print(self.learning_rate)
        print(self.threshold)
        print(self.bias)
        print(self.matrix)

    def compute(self):
        print(self.matrix)
        for indexRow in range(len(self.matrix)):
            row = self.matrix[indexRow]
            print(self.computePerceptronValue(row))
            row[self.indexA] = self.computePerceptronValue(row)
            row[self.indexY] = self.determineY(row[self.indexA])
            if(indexRow != len(self.matrix)-1):
                self.matrix[indexRow+1][3:6] = self.adjustWeight(row)

        for x in self.matrix:
            print(x)


p = Perceptron()
p.readInput()
p.compute()