import itertools
import sys


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
                print("Error: Invalid input matrix")
                sys.exit()

            # get the index of the values a, y, z in the table
            self.indexA = self.inputRowLength * 2
            self.indexY = self.indexA + 1
            self.indexZ = self.indexY + 1

    def computePerceptronValue(self, row: list) -> float:
        a = 0
        for i in range(self.inputRowLength):
            a += row[i] * row[self.inputRowLength + i]
        return a

    def determineY(self, a: float) -> float:
        return 1 if a >= self.threshold else 0

    def adjustWeight(self, row: list) -> list:
        # computes for the weights of the next row
        output = []
        for i in range(self.inputRowLength):
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

    def stringMatrix(self) -> str:
        # generate a string of a formatted matrix
        matrix = ""
        subscript = [str(x) for x in range(self.inputXLength)]
        subscript.append("b")
        label = list(
            map(lambda x: "".join(x), itertools.product(["x", "w"], subscript))
        )
        label = label + ["a", "y", "z"]

        formatString = "{:4s} " * len(label)
        matrix += formatString.format(*label)
        matrix += "\n"

        formatString = "{:<4.1f} " * len(self.matrix[0])
        for row in self.matrix:
            matrix += formatString.format(*row)
            matrix += "\n"
        return matrix

    def printMatrix(self):
        print(self.stringMatrix())

    def compute(self):
        # compute the perceptron
        stopFlag = False
        interations = 0
        outputMatrix = ""

        # loop until the weights converge
        while not stopFlag:
            lastrow = []
            for indexRow in range(len(self.matrix)):
                row = self.matrix[indexRow]
                row[self.indexA] = self.computePerceptronValue(row)
                row[self.indexY] = self.determineY(row[self.indexA])
                if indexRow != len(self.matrix) - 1:
                    self.matrix[indexRow + 1][
                        self.inputRowLength : self.inputRowLength * 2
                    ] = self.adjustWeight(row)
                else:
                    lastrow = self.adjustWeight(row)

            # checks for the weights if it converged
            for indexRow in range(1, len(self.matrix)):
                if (
                    self.matrix[indexRow][self.inputRowLength : self.inputRowLength * 2]
                    != lastrow
                ):
                    stopFlag = False
                    break
                stopFlag = True

            # if the weights does not converge update the first row weights with the lastrow
            if not stopFlag:
                self.matrix[0][self.inputRowLength : self.inputRowLength * 2] = lastrow

            interations += 1
            outputMatrix += "Iteration: " + str(interations) + "\n"
            outputMatrix += self.stringMatrix()

        with open("output.txt", "w") as file:
            file.write(outputMatrix)


if __name__ == "__main__":
    p = Perceptron()
    p.readInput()
    p.compute()
