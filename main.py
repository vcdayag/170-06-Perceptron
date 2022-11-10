class Perceptron:
    def __init__(self):
        self.learning_rate = 0.1
        self.threshold = 0.5
        self.bias = 1
        self.matrix = []
        self.inputRowLength = 0
        self.inputXLength = 0
        self.indexA = 0
        self.indexY = 0
        self.indexZ = 0

    def readInput(self):
        with open("input.txt", "r") as inputFile:
            inputList = [x.strip() for x in inputFile]
            self.learning_rate = float(inputList.pop(0))
            self.threshold = float(inputList.pop(0))
            self.bias = float(inputList.pop(0))

            try:
                for row in inputList:
                    rowList = [float(x) for x in row.split()]
                    self.inputRowLength = len(rowList)
                    self.inputXLength = self.inputRowLength - 1
                    if len(inputList) != 2**self.inputXLength:
                        raise IndexError
                    # add the b in matrix
                    rowList[self.inputXLength : self.inputXLength] = [self.bias]
                    # add the w0 ... wb columns and also the a and y columns
                    rowList[self.inputRowLength : self.inputRowLength] = [
                        0.0 for _ in range(self.inputRowLength + 2)
                    ]
                    self.matrix.append(rowList)
            except IndexError as e:
                print("Error: Invalid self.matrix")

            self.indexA = self.inputRowLength * 2
            self.indexY = self.indexA + 1
            self.indexZ = self.indexY + 1

    def computePerceptronValue(self, row: list) -> float:
        a = 0
        for i in range(self.inputRowLength):
            a += row[i] * row[self.inputRowLength + i]
        return a

    def determineY(self, a: float) -> float:
        return 1.0 if a >= self.threshold else 0.0

    def adjustWeight(self, row: list) -> list:
        output = []
        for i in range(self.inputRowLength):
            print(
                "".join(
                    [
                        str(row[self.inputRowLength + i]),
                        "+",
                        str(self.learning_rate),
                        "*",
                        str(row[i]),
                        "*(",
                        str(row[self.indexZ]),
                        "-",
                        str(row[self.indexY]),
                        ")=",
                        str(
                            row[self.inputRowLength + i]
                            + (
                                self.learning_rate
                                * row[i]
                                * (row[self.indexZ] - row[self.indexY])
                            )
                        ),
                    ]
                )
            )
            output.append(
                row[self.inputRowLength + i]
                + (self.learning_rate * row[i] * (row[self.indexZ] - row[self.indexY]))
            )
        return output

    def debugprint(self):
        print(self.learning_rate)
        print(self.threshold)
        print(self.bias)
        self.printMatrix()

    def printMatrix(self):
        for x in self.matrix:
            print(x)
        print()

    def compute(self):
        stopFlag = False
        interations = 0
        self.printMatrix()

        while not stopFlag:
            lastrow = []
            for indexRow in range(len(self.matrix)):
                row = self.matrix[indexRow]
                row[self.indexA] = self.computePerceptronValue(row)
                # print(self.indexA)
                # print(row[self.indexA])
                row[self.indexY] = self.determineY(row[self.indexA])
                if indexRow != len(self.matrix) - 1:
                    # print("adjustweight "+str(self.adjustWeight(row)))
                    self.matrix[indexRow + 1][
                        self.inputRowLength : self.inputRowLength * 2
                    ] = self.adjustWeight(row)
                else:
                    lastrow = self.adjustWeight(row)

                # print("edit row")
                # print(row)

            for indexRow in range(1, len(self.matrix)):
                # print(
                #     self.matrix[indexRow][self.inputRowLength : self.inputRowLength * 2]
                # )
                # print(lastrow)
                # print()
                if (
                    self.matrix[indexRow][self.inputRowLength : self.inputRowLength * 2]
                    != lastrow
                ):
                    stopFlag = False
                    break
                stopFlag = True

            if not stopFlag:
                self.matrix[0][self.inputRowLength : self.inputRowLength * 2] = lastrow

            interations += 1
            print("iteration:", interations)
            self.printMatrix()

            # if interations == 7:
            # return


p = Perceptron()
p.readInput()
# p.debugprint()
p.compute()
