import numpy as np
import matplotlib.pyplot as plt

def prepare(X,y,w):
    """
    Функкция создаёт график для последующего изменения
    Атрибуты
    --------
    prepare.X1min
    prepare.X1max
    prepare.fig
    prepare.ax
    prepare.line

    """
    X_ = X.tolist()
    X_.sort(key = lambda x: x[0])
    X1min = X_[0][0]
    X1max = X_[-1][0]
    prepare.X1min = X1min
    prepare.X1max = X1max
    
    X_.sort(key = lambda x: x[1])
    X2min = X_[0][1]
    X2max = X_[-1][1]
    
    prepare.fig, prepare.ax = plt.subplots()
    prepare.ax.set_title("Начало")
    prepare.ax.set_xlim([X1min - 1, X1max + 1])
    prepare.ax.set_ylim([X2min - 1, X2max + 1])

    x1 = X1min
    y1 = (-w[0] - x1*w[1])/w[2] # 1 точка (x1, y1)

    x2 = X1max
    y2 = (-w[0] - x2*w[1])/w[2] # 2 точка (x2, y2)

    prepare.line = prepare.ax.plot([x1,x2], [y1,y2])
    for i in range(len(y)):
            if y[i] == 1:
                prepare.ax.scatter(X[i][0],X[i][1], c = 'r')
            else:
                prepare.ax.scatter(X[i][0],X[i][1], c = 'b')


def visual(X, y, w, poc): #визуал
    """
    Функция перересовывает прямую с обновлёнными весами
    1*w0 + X1*w1 + X2*w2 = 0
    """
    prepare.ax.set_title("Поколение {}".format(poc))
    
    x1 = prepare.X1min
    y1 = (-w[0] - x1*w[1])/w[2] # 1 точка (x1, y1)

    x2 = prepare.X1max
    y2 = (-w[0] - x2*w[1])/w[2] # 2 точка (x2, y2)

    prepare.line.pop(0).remove()
    prepare.line = prepare.ax.plot([x1,x2], [y1,y2])
    
    plt.pause(0.001)
    

    
class Perceptron:
    """ Классификатор на основе персептрона.

    Параметры
    ---------
    eta : float
        Скорость обучения [0.0, 1.0]
    n_iter : int
        Проходы по обучающему набору данных.
    random_state : int
        Начальное значение генератора случайных чисел
        для инициализации случайными весами.

    Атрибуты
    --------
    w_ : одномерный массив
        Веса после подгонки.
    errors_ : список
        Количество неправильных классификаций (обновлений) в каждой эпохе.
    """
    def __init__(self, eta = 0.01, n_iter = 50, random_state = 1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """ Подгоняет к обучающим данным.
        Параметры
        ---------
        X : {подобен массиву}, форма = [n_examples, n_features]
            Обучающие векторы, где n_examples - количество образцов
            и n_features - количество признаков.
        y : подобен массиву, форма = [n_examples]
            Целевые значения.
        Возвращает
        ----------
        self : object
        """
        rgen = np.random.RandomState(self.random_state) # инициализирует генератор
        self.w_ = rgen.normal(loc = 0.0, scale = 0.01,
                              size = 1 + X.shape[1]) # loc - центр распределения
        self.errors_ = []
        prepare(X,y,self.w_) #визуал
        for poc in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
                if update != 0.0:
                    visual(X,y,self.w_, poc) #визуал
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Вычисляет общий вход"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """Возврщает метку класса после единичного шага"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)


def main():
    import pandas as pd
    global df
    df = pd.read_csv(r'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                     header = None,
                     encoding = 'utf-8')
    for i in range(len(df)):
        if df.loc[i, 4] == 'Iris-setosa':
            df.loc[i, 4] = 1
        else:
            df.loc[i, 4] = -1
    data = df.to_numpy(dtype = float)
    #data 5 столбцов, столбцы 0 и 1 не сепарабельны
    X = data[:, [0,1]]
    y = data[:, -1]
    p1 = Perceptron()
    p1.fit(X,y)


def my1():
    
    X = np.array([[1,2],
                  [3.5,6],
                  [3,4],
                  [2,7],
                  [7,8],
                  [9,10],
                  [7,4],
                  [8,7]])

    y = np.array([1,
                  1,
                  1,
                  1,
                  -1,
                  -1,
                  -1,
                  -1])
    
    p1 = Perceptron(n_iter = 7)
    p1.fit(X,y)
    print(p1.errors_)
    
           
if __name__ == '__main__':
    main()
    
