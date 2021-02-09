import shipilov
from random import randint
import matplotlib.pyplot as plt

def exec_subtask1():

    list_values = []
    for i in range(10):
        list_values.append(randint(0,1000))
    n, bins, patches = plt.hist(list_values, 10)
    plt.show()

if __name__ == '__main__':
    exec_subtask1()
