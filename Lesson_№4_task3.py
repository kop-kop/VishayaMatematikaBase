import shipilov
from math import sin, cos
import matplotlib.pyplot as plt


class Line_segment:
    length_beetwen_lines_on_canvas = 10
    length = 0
    angle_alfa = 0
    x_start = 0
    y_start = 0
    x_finish = 0
    y_finish = 0

    def __init__(self):
        while True:
            res = shipilov.input_(
                text_dialog="Введите через пробел следующие целочисленнные параметры:\n"
                            "- расстояние между линиями холста\n"
                            "- длину игры\n"
                            "- координаты нижней точки иглы в формате x,y\n"
                            "- угол наклона иглы\n"
                            "Пример: 10 20 5,11 45\n",
                only_positive=False, str_numbers='')
            try:
                res_list = res.split(" ")
                self.length_beetwen_lines_on_canvas = int(res_list[0])
                self.length = int(res_list[1])
                xy = res_list[2].split(",");
                self.x_start = int(xy[0])
                self.y_start = int(xy[1])
                self.angle_alfa = int(res_list[3])
                self.x_finish = self.x_start + (self.length * cos(self.angle_alfa))
                self.y_finish = self.y_start + (self.length * sin(self.angle_alfa))
            except:
                print("Некорректный ввод. Повторите попытку")
                continue
            else:
                break

    def __str__(self):
        return f'Длина отрезка {self.length}, координаты ({str(round(self.x_start, 3))},{str(round(self.y_start, 3))})({str(round(self.x_finish, 3))},{str(round(self.y_finish, 3))}), угол {self.angle_alfa}.\n' \
               f'Расстояние между линиями сетки {self.length_beetwen_lines_on_canvas}'
        #str(round( , 3))


def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    n = 0
    if not y2 - y1 == 0:  # a(y)
        q = (x2 - x1) / (y1 - y2)
        sn = (x3 - x4) + (y3 - y4) * q  # c(x) + c(y)*q
        if not sn:
            return 0
        fn = (x3 - x1) + (y3 - y1) * q  # b(x) + b(y)*q
        n = fn / sn
    else:
        if not y3 - y4:
            return 0  # b(y)
        n = (y3 - y1) / (y3 - y4)  # c(y)/b(y)
    cross_x = x3 + (x4 - x3) * n  # x3 + (-b(x))*n
    cross_y = y3 + (y4 - y3) * n  # y3 +(-b(y))*n
    return [cross_x, cross_y]


def exec_subtask3():

    line = Line_segment()

    fig, ax = plt.subplots()

    # рисуем сетку
    coords_x = [-300, 300]
    for i in range(-50, 50, 1):
        o = i * line.length_beetwen_lines_on_canvas;
        coords_y = [o, o]
        ax.plot(coords_x, coords_y, color="#9900CC")
    coords_y = [-300, 300]
    for i in range(-50, 50, 1):
        o = i * line.length_beetwen_lines_on_canvas;
        coords_x = [o, o]
        ax.plot(coords_x, coords_y, color="#9900CC")

    # определяем ближайшие отрезки сетки к левому концу иглы
    # 1. определим левый конец иглы
    if line.x_start <= line.x_finish:
        left_x = line.x_start
        left_y = line.y_start
    else:
        left_x = line.x_finish
        left_y = line.y_finish
    # 2. определим отрезки сетки вокруг точки (left_x,left_y)
    # координата x отрезка справа
    right_grid_x = shipilov.round_to_a_multiple(left_x, line.length_beetwen_lines_on_canvas)
    if right_grid_x < left_x:
        right_grid_x += line.length_beetwen_lines_on_canvas
    # координата y отрезка сверху
    top_grid_y = shipilov.round_to_a_multiple(left_y, line.length_beetwen_lines_on_canvas)
    if top_grid_y < left_y:
        top_grid_y += line.length_beetwen_lines_on_canvas
    # координаты y отрезка справа
    right_grid_y_start = top_grid_y - line.length_beetwen_lines_on_canvas
    right_grid_y_finish = top_grid_y
    # координаты x отрезка сверху
    top_grid_x_start = right_grid_x - line.length_beetwen_lines_on_canvas
    top_grid_x_finish = right_grid_x
    # координаты отрезка слева
    left_grid_x = top_grid_x_start
    left_grid_y_start = right_grid_y_start
    left_grid_y_finish = right_grid_y_finish
    # координаты отрезка снизу
    bottom_grid_y = right_grid_y_start
    bottom_grid_x_start = top_grid_x_start
    bottom_grid_x_finish = top_grid_x_finish

    # ищем точки пересечения
    cross_right = cross(line.x_start, line.y_start, line.x_finish, line.y_finish, right_grid_x, right_grid_y_start,
                        right_grid_x, right_grid_y_finish)
    cross_top = cross(line.x_start, line.y_start, line.x_finish, line.y_finish, top_grid_x_start, top_grid_y,
                      top_grid_x_finish, top_grid_y)
    cross_left = cross(line.x_start, line.y_start, line.x_finish, line.y_finish, left_grid_x, left_grid_y_start,
                       left_grid_x, left_grid_y_finish)
    cross_bottom = cross(line.x_start, line.y_start, line.x_finish, line.y_finish, bottom_grid_x_start, bottom_grid_y,
                         bottom_grid_x_finish, bottom_grid_y)
    if not cross_right == 0:
        cross_list_str = f'({str(round(cross_right[0], 3))},{str(round(cross_right[1], 3))})'
        ax.scatter(cross_right[0], cross_right[1], label=cross_list_str)
    if not cross_top == 0:
        cross_list_str = f'({str(round(cross_top[0], 3))},{str(round(cross_top[1], 3))})'
        ax.scatter(cross_top[0], cross_top[1], label=cross_list_str)
    if not cross_left == 0:
        cross_list_str = f'({str(round(cross_left[0], 3))},{str(round(cross_left[1], 3))})'
        ax.scatter(cross_left[0], cross_left[1], label=cross_list_str)
    if not cross_bottom == 0:
        cross_list_str = f'({str(round(cross_bottom[0], 3))},{str(round(cross_bottom[1], 3))})'
        ax.scatter(cross_bottom[0], cross_bottom[1], label=cross_list_str)

    # рисуем отрезок
    coords_x = [line.x_start, line.x_finish]
    coords_y = [line.y_start, line.y_finish]
    ax.plot(coords_x, coords_y, label=line, marker="o")
    ax.legend()
    plt.show()

if __name__ == '__main__':
    exec_subtask3()
