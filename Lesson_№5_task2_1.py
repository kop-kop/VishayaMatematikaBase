import shipilov

def exec_subtask2_1():
    while True:
        res = shipilov.input_(
            text_dialog="Какова вероятность что на обеих рулетках казино (в каждой по 38 cекторов) выпадут числа из диапазона:\n"
                        "(Пример ввода: 2-15)",
            only_positive=False, str_numbers='')
        try:
            res_list = res.split("-")
            a = int(res_list[0])
            b = int(res_list[1])
            if a>b or b-a>38 or a>38 or b>38 or a<0 or b<0:
                raise
            else:
                res = ((b-a) / 38) ** 2
        except:
            print("Некорректный ввод. Повторите попытку")
            continue
        else:
            print(f'Вероятность этого события составит {str(round(res, 3))}')
            res = shipilov.select_value_from_list(["Да", "Нет"], "Хотите сделать рассчёт еще раз?")
            if res == "Нет":
                quit()

if __name__ == '__main__':
    exec_subtask2_1()
