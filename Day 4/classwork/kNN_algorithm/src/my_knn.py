import csv
import math
from collections import Counter
import os

filename = os.getcwd() + '/src/iris.csv'


class MyKnn(object):

    def __init__(self, k_value):
        self.filename = filename
        self.trainingset = None
        self.k = k_value
        self.preprocess_dataset()
        self.class_labels = {
            0: 'Setosa',
            1: 'Versicolor',
            2: 'Virginica'
        }

    def preprocess_dataset(self):
        data = [row for row in csv.reader(open(self.filename))]
        data = data[1:]
        data = [
            [
                float(item[0]), 
                float(item[1]), 
                float(item[2]), 
                float(item[3]),
                int(item[4])]
            for item in data]
        self.trainingset = data

    def euclideandistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)

    def getNeighbors(self, testInstance):
        distances = []
        length = len(testInstance) - 1
        for training_instance in (self.trainingset):
            dist = self.euclideandistance(testInstance, training_instance, length)
            distances.append((training_instance[4], dist))
        distances.sort(key=lambda x:x[1])
        neighbours = []
        for x in range(self.k):
            neighbours.append(distances[x][0])
        return neighbours

    def prediction(self, testInstance):
        neighbours = self.getNeighbors(testInstance)
        prediction = Counter(neighbours).most_common(1)[0][0]
        prediction = self.class_labels.get(prediction)
        return prediction


if __name__ == '__main__':
    print(MyKnn(3).prediction([5.5, 2.4, 3.8, 1.1]))


