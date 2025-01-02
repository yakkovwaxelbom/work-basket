import random
import numpy as np





class KMeans:
    def __init__(self, samples, k: int, d=3) -> None:
        self.samples = samples
        self.k = k
        self.d = d
        # number of clusters
        self.means = np.random.randint(0, 255, (k, d))
        self.clusters = None

    def __classify(self):
        self.clusters = np.array([np.argmin(np.sum((sample - self.means) ** 2, axis=1))
                                  for sample in self.samples])

    def __mean(self, ):
        new_means = []
        location_each_cluster = [[] for _ in range(self.k)]
        for i, cluster in enumerate(self.clusters):
            location_each_cluster[cluster].append(i)

        for item in location_each_cluster:
            new_means.append(np.array(np.mean(self.samples[item], axis=0) if item else random.choice(self.samples)))
        return np.array(new_means)

    def train(self):
        self.__classify()
        nwe_mean = self.__mean()
        while not np.array_equal(nwe_mean, self.means):
            self.means = nwe_mean
            self.__classify()
            nwe_mean = self.__mean()
        return self.means, self.clusters



a =np.array([[1, 2, 3], [2, 6, 4]])

b =np.array([[1, 2, 3], [2, 3, 4]])
#
while not np.array_equal(a, b):
    print('ok')
