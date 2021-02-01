def input_(only_positive=True, str_numbers='1234567890', text_dialog=""):
    while True:
        str_value = input(f'{text_dialog} : ')
        if not str_numbers == '':
            invalid_character = False
            if only_positive:
                for character in str_value:
                    if str_numbers.find(character) == -1:
                        print('Введен недопустимый символ. Попробуйте снова.')
                        invalid_character = True
                        break
            else:
                i = 0
                for character in str_value:
                    if str_numbers.find(character) == -1 and not (i == 0 and character == "-"):
                        print('Введен недопустимый символ. Попробуйте снова.')
                        invalid_character = True
                        break
                    i = i + 1
            if invalid_character:
                continue
            else:
                return str_value
        else:
            return str_value

def attrs_of_class(cls):
    """
    Возвращает список атрибутов класса в т.ч. родительского класса
    :param cls:
    :return: list
    """
    import inspect
    # получаем ряд свойств класса
    attrs = inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
    # фильтруем полученные свойства, оставляя только определенные разработчиком атрибуты класса (в т.ч. родительского класса)
    attrs = [a[0] for a in attrs if not (a[0].startswith('__') and a[0].endswith('__'))]
    return attrs

def attrs_of_class_with_types(cls,exclude_attrs_of_parent_class = False,attributes_to_save = []):
    """
    Возвращает словарь атрибутов класса вида "название атрибута"-"тип значения атрибута".
    Параметр exclude_attrs_of_parent_class определяет необходимость исключения попадания в словарь атрибутов родителя.
    Параметр attributes_to_save содержит название атрибутов, которые необходимо сохранить при исключении атрибутов родителя.
    :param cls: class, exclude_attrs_of_parent_class: boolean, attributes_to_save: list
    :return: dict
    """
    import inspect
    # получаем ряд свойств класса
    attrs_list = inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
    # фильтруем полученные свойства, оставляя только определенные разработчиком атрибуты класса (в т.ч. родительского класса)
    attrs_list = [a for a in attrs_list if not (a[0].startswith('__') and a[0].endswith('__'))]
    if exclude_attrs_of_parent_class:
        parents = cls.__bases__
        for parent in parents:
            if not inspect.isclass(parent):
                continue
            attrs_keys = attrs_of_class_with_types(parent,True,attributes_to_save).keys()
            if not len(attrs_keys):
                break
            attrs_index_list_remove = []
            for i in range(len(attrs_list)):
                attr = attrs_list[i]
                if attr[0] in attrs_keys and not attr[0] in attributes_to_save:
                    attrs_index_list_remove.append(i)
            attrs_list = [x for i,x in enumerate(attrs_list) if i not in attrs_index_list_remove]
    attrs_dict = {}
    for attr in attrs_list:
        attrs_dict[attr[0]] = type(attr[1])
    return attrs_dict

def select_value_from_list(list_value,text_dialog="Choose from the available values"):
    count_ = len(list_value)
    question_text = text_dialog
    for index_ in range(count_):
        question_text += "\n" + str(index_ + 1) + ". " + str(list_value[index_])
    question_text += "\n"
    select_index_ = 0
    while True:
        err = False
        try:
            select_index_ = int(
                input_(str_numbers="123456789", only_positive=True, text_dialog=question_text))
            select_index_ = select_index_ - 1
            if select_index_ < 0 or select_index_ >= count_:
                raise
        except:
            print("It was not possible to determine what you need to select from the entered number. Please try again...")
            err = True
            continue
        if not err:
            break
    return list_value[select_index_]

def rand_name(length_name=0):
    from random import randint
    bc = "bcdfghjklmnpqrstvwxz"
    ae = "aeiouy"
    res = ""
    max_index_bc = len(bc) - 1
    max_index_ae = len(ae) - 1
    iter_value = range(randint(4, 10)) if length_name == 0 else range(length_name)
    if len(iter_value)>=3:
        for i in iter_value:
            k = randint(0, 2)
            if k > 0:
                res = res + bc[randint(1, max_index_bc)]
            else:
                res = res + ae[randint(1, max_index_ae)]
    res = bc[randint(1, max_index_bc)].upper() + ae[randint(1, max_index_ae)] + res
    return res