import matplotlib.pyplot as plt
import math
import pandas as pd

def SpreadAndRegression(dataX, dataY, a, b):
    F = []
    for i in range(0, len(dataX)):
        F.append((dataY[i] * a + b))

    plt.plot(dataX,F)
    plt.plot(dataX, dataY, 'go')
    plt.show()


def Mean(dataNums):
    return (float)(1 / len(dataNums)) * sum(dataNums)


def MeanForMul(dataNums1, dataNums2):
    sumNum = 0
    for i in range(len(dataNums1)):
        sumNum += dataNums2[i] * dataNums1[i]
    return (float)(1 / len(dataNums1)) * sumNum


def Variation(dataNums):
    sumNum = 0.0
    for i in range(len(dataNums)):
        sumNum += (dataNums[i] - Mean(dataNums)) ** 2
    return ((1 / len(dataNums)) * sumNum)


def Correlation(dataX, dataY):
    return ((MeanForMul(dataX, dataY) - (Mean(dataX) * Mean(dataY))) / math.sqrt(Variation(dataX) * Variation(dataY)))


def Average(data):
    return ((1 / len(data)) * sum(data))


def Regression(a, b, y):
    return a * y + b


data = pd.read_excel(r'r4z2.xlsx')
dataX = []
dataY = []

for index, rows in data.iterrows():
    dataX.append(rows.X)
    dataY.append(rows.Y)

aX = Correlation(dataX, dataY) * (Variation(dataX) / Variation(dataY))
bX = Average(dataX) - Average(dataY) * aX

aY = Correlation(dataX, dataY) * (Variation(dataY) / Variation(dataX))
bY = Average(dataY) - Average(dataX) * aY

SpreadAndRegression(dataX, dataY, aX, bX)

print("Уравнение линейной регрессии X по Y: x =", Average(dataX), "+", Correlation(dataX, dataY), "*", Variation(dataX),
      "/", Variation(dataY), "*(y -", Average(dataY), ")")
print("Уравнение линейной регрессии Y по X: y =", Average(dataY), "+", Correlation(dataX, dataY), "*", Variation(dataY),
      "/", Variation(dataX), "*(x -", Average(dataX), ")")
print("Коэффиценты линейной регрессии X по Y: (", aX, ",", bX, ")")
print("Коэффиценты линейной регрессии Y по X: (", aY, ",", bY, ")")
print("Прогноз X по значению Y при Y=80:", Regression(aX, bX, 80))

