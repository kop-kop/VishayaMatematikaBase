import shipilov
from random import randint

def exec_subtask1():

    list_cells = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, "00", 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
    max_count = len(list_cells)-1
    while True:
        res = list_cells[randint(0,max_count)]
        print(f'Вам выпал сектор {res}')
        res = shipilov.select_value_from_list(["Да", "Нет"], "Хотите попробовать еще раз?")
        if res == "Нет":
            quit()

if __name__ == '__main__':
    exec_subtask1()
