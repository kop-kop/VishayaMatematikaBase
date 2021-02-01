import shipilov
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randint
from math import sqrt

class Vector:
    name = ""
    length = 0
    x_finish = 0
    y_finish = 0
    z_finish = 0
    x_start = 0
    y_start = 0
    z_start = 0

    def __init__(self, name=None, start=None, finish=None):
        if name is None:
            name = shipilov.rand_name(randint(2, 6))
        self.name = name
        while True:
            if finish is None:
                coords_finish = shipilov.input_(only_positive=False, str_numbers='',
                                                text_dialog=f'Введите координаты x,y,z для вектора {name}')
            else:
                coords_finish = finish
            try:
                if type(coords_finish[0]) == type(""):
                    self.coords_finish = list(map(float, coords_finish.split(",")))
                else:
                    self.coords_finish = coords_finish
                if not start is None:
                    self.x_start = float(start[0])
                    self.y_start = float(start[1])
                    self.z_start = float(start[2])
            except:
                print("Некорректный ввод. Повторите попытку")
                continue
            else:
                self.coords_start = [self.x_start, self.y_start, self.z_start]
                self.x_finish = self.coords_finish[0]
                self.y_finish = self.coords_finish[1]
                self.z_finish = self.coords_finish[2]
                break
        self.length = sqrt(abs(((self.x_finish ** 2) + (self.y_finish ** 2) + (self.z_finish ** 2)) - (
                (self.x_start ** 2) + (self.y_start ** 2) + (self.z_start ** 2))))

    def __str__(self):
        return self.name + ", length: " + str(round(self.length, 3))


def operations():
    operations = []
    operation_element = {"Сложить 2 вектора": sum_vectors}
    operations.append(operation_element)
    operation_element = {"Узнать длину вектора по координатам": vector_length}
    operations.append(operation_element)
    return operations


def size_canvas_for_vectors(vectors_list, direction_of_the_coordinate="x"):
    default_size = [-10, 15]
    size_ = default_size.copy()
    check_values = [sum([getattr(vector, direction_of_the_coordinate + "_start") for vector in vectors_list]),
                    sum([getattr(vector, direction_of_the_coordinate + "_finish") for vector in vectors_list])]
    for check_value in check_values:
        if check_value < size_[0]:
            size_[0] = check_value - 15
        if check_value > size_[1]:
            size_[1] = check_value + 15
    return size_


def sum_vectors():
    # считаем сумму
    a = Vector("a")
    b = Vector("b", start=[a.x_finish, a.x_finish, a.z_finish])
    c = Vector("c", start=[k + j for k, j in zip(a.coords_start, b.coords_start)],
               finish=[k + j for k, j in zip(a.coords_finish, b.coords_finish)])

    # готовим пространство для рисования
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # задаём размеры пространства в зависимости от масшабов векторов
    vectors_list = [a, b, c]
    ax.set_zlim(size_canvas_for_vectors(vectors_list, "z"))
    ax.set_ylim(size_canvas_for_vectors(vectors_list, "y"))
    ax.set_xlim(size_canvas_for_vectors(vectors_list, "x"))

    # рисуем вектора в пространстве
    ax.quiver(a.x_start, a.y_start, a.z_start, a.x_finish, a.y_finish, a.z_finish, color="#9900CC", label=a)
    ax.quiver(b.x_start, b.y_start, b.z_start, b.x_finish, b.y_finish, b.z_finish, color="#33CC33", label=b)
    ax.quiver(c.x_start, c.y_start, c.z_start, c.x_finish, c.y_finish, c.z_finish, color="#FF9900", label=c)

    plt.legend()
    plt.show()


def vector_length():
    a = Vector("a")

    # готовим пространство для рисования
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # задаём размеры пространства в зависимости от масшабов векторов
    vectors_list = [a]
    ax.set_zlim(size_canvas_for_vectors(vectors_list, "z"))
    ax.set_ylim(size_canvas_for_vectors(vectors_list, "y"))
    ax.set_xlim(size_canvas_for_vectors(vectors_list, "x"))

    # рисуем вектора в пространстве
    ax.quiver(a.x_start, a.y_start, a.z_start, a.x_finish, a.y_finish, a.z_finish, color="#9900CC", label=a)

    plt.legend()
    plt.show()


def exec_subtask2():
    operations_list = operations()
    count_operations = len(operations_list)
    question_text = "Введите номер операции, которую хотите произвести над векторами:"
    for index_operation in range(count_operations):
        question_text += "\n" + str(index_operation + 1) + ". " + list(operations_list[index_operation].keys())[0]
    select_index_operation = 0

    while True:
        try:
            index_operation = int(
                shipilov.input_(str_numbers="123456789", only_positive=True, text_dialog=question_text))
            select_index_operation = index_operation - 1
            if select_index_operation < 0 or select_index_operation >= count_operations:
                raise
            else:
                operation = list(operations_list[select_index_operation].values())[0]
                operation()
        except:
            print("Не удалось определить операцию по введенному номеру. Повторите еще раз, пожалуйста...")


if __name__ == '__main__':
    exec_subtask2()
