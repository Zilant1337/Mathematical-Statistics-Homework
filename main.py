import pandas
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import numpy as np

def Histogram(standartVariation, sampleMean, sampleVarianceBiased, data, minVar, maxVar, sampleRange):
    sampleSize = len(data)
    sortedData = sorted(data)

    #нормальное распределение
    normalSpread = []
    for i in range(0, len(sortedData)):
        normalSpread.append(
            (1 / (standartVariation * math.sqrt(2 * math.pi))) * math.exp(-((sortedData[i] - sampleMean) * (sortedData[i] - sampleMean) / (2 * sampleVarianceBiased))))

    interval = (round)(sampleSize / 10)
    a = []
    delt = sampleRange / (interval - 1)
    a.append(115)   #минимальная граница a_0
    a.append(minVar + delt / 2)  # a1
    for i in range(1, interval - 1):
        a.append(a[i] + delt)
    a.append(maxVar - delt / 2)  # a(k-1)
    a.append(125)   #максимальная граница a_k

    h = []  #высоты
    sum = 0
    modeStart=0
    for j in range(1, len(a)):
        for i in range(0, len(data)):
            if data[i] >= a[j - 1] and data[i] < a[j]:
                sum += 1
        h.append(sum / (sampleSize * (a[j] - a[j - 1])))
        if sum / (sampleSize * (a[j] - a[j - 1])) == max(h):
            modeStart=a[j-1]
        sum = 0
    mode=modeStart+delt/2

    print ("Мода:", mode)
    plt.plot(sortedData, normalSpread)
    plt.stairs(h, a, fill=True)
    plt.show()

def Distribution(data):
    sortedData = sorted(data)
    sampleSize = len(data)
    F = []
    sum = 0
    #вычисление ЭФР
    for i in range(0, len(sortedData)):
        for j in range(0, len(sortedData)):
            if sortedData[j] < sortedData[i]:
                sum += 1
        F.append(sum / sampleSize)
        sum = 0
    plt.step(sortedData, F, color="green")
    plt.show()
#вычисление q квантиля с заданным параметром
def qQuantile(dataNums,q):
    x=(len(dataNums)-1)*q+1

    if (len(dataNums)%2!=0):
        return dataNums[(int)(x)]

    return (dataNums[(int)(x)]+dataNums[(int)(x+1)])/2
#вычисление выборочного среднего
def Mean(dataNums):
    return (float)(1/len(dataNums))*sum(dataNums)
#вычисление смешённой выборочной дисперсии
def Variance(dataNums):
    sumNum=0.0
    for i in range (len(dataNums)):
        sumNum+=(dataNums[i]-Mean(dataNums))**2
    return (float)(1/len(dataNums))*sumNum
#вычисление коэффицента асимметрии
def Asymmetry(dataNums, variation):
    sumNum = 0.0
    for i in range(len(dataNums)):
        sumNum += (dataNums[i] - Mean(dataNums)) ** 3
    return (float)(1 / (len(dataNums)*(variation ** 3))) * sumNum
#вычисление коэффицента эксцесса
def Excess(dataNums, variation):
    sumNum = 0.0
    for i in range(len(dataNums)):
        sumNum += (dataNums[i] - Mean(dataNums)) ** 4
    return ((float)(1 / (len(dataNums) * (variation ** 4))) * sumNum)-3
#вычисление медианы
def Median(dataNums):
    dataSorted=sorted(dataNums)
    return qQuantile(dataSorted,0.5)

data = pandas.read_csv("r1z1.csv")
dataNum = []

for index, rows in data.iterrows():
    dataNum.append(rows.X)

sampleSize= len(dataNum)
maxVar= max(dataNum)
minVar= min(dataNum)
sampleRange = maxVar-minVar

sampleMean = Mean(dataNum)
sampleVarianceBiased = Variance(dataNum)
sampleVarianceUnbiased = (float)(len(dataNum)/(len(dataNum)-1))*(sampleVarianceBiased)
standartVariation = math.sqrt(sampleVarianceBiased)

asymmetryCoefficient= Asymmetry(dataNum,standartVariation)

excessCoefficient = Excess(dataNum,standartVariation)

median=Median(dataNum)

interquartileDistance= qQuantile(sorted(dataNum),3/4)-qQuantile(sorted(dataNum),1/4)



print("Максимум:", maxVar, "Минимум:", minVar, "Объём выборки:",sampleSize, "Размах выборки:", sampleRange, "Выборочное среднее:",sampleMean, "Выборочная дисперсия (не смещённая):", sampleVarianceUnbiased, "Выборочная дисперсия (смещённая):", sampleVarianceBiased, "Стандартное отклонение:",standartVariation,"Коэфицент асимметрии:", asymmetryCoefficient,"Коэфицент эксцесса:", excessCoefficient,"Выборочная медиана:", median, "Интерквартильная широта:", interquartileDistance)



Histogram(standartVariation, sampleMean, sampleVarianceBiased, dataNum, minVar, maxVar, sampleRange)
#!!!Чтобы посмотреть второй график, закройте первый!!!
Distribution(dataNum)


