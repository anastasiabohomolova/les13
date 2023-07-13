class One:
    def __init__(self, *args):
        super().__init__()
        self.args = args

        el_l = list(args)
        el_d = dict.fromkeys(el_l, 'factory')

        lst_for_key = []
        lst_for_value = []
        for i in el_d.keys():
            lst_for_key.append(i)
        for i in el_d.values():
            if isinstance(i, list) or isinstance(i, dict):
                i = tuple(i)
                lst_for_value.append(i)
                v_set = set(lst_for_value)
                print('value set with dict or list from class Two', v_set)
                break
            else:
                lst_for_value.append(i)


        key_set = set(lst_for_key)
        value_set = set(lst_for_value)
        print('set keys for class One: ', key_set)
        print('set values for class One: ', value_set)


class Two(One):
    def __init__(self, *args):
        self.args = args
        el_l = list(args)
        el_d = dict.fromkeys(el_l, {1: 30250, 'age':5})

        lst_for_key = []
        lst_for_value = []
        for i in el_d.keys():
            lst_for_key.append(i)
        for i in el_d.values():
            if isinstance(i, list) or isinstance(i, dict):
                i = tuple(i)
                lst_for_value.append(i)
                v_set = set(lst_for_value)
                print('value set with dict or list from class Two', v_set)
                break
            else:
                lst_for_value.append(i)

        key_set = set(lst_for_key)
        print('set keys for class Two: ', key_set)
        value_set = set(lst_for_value)
        print('set values for class Two: ', value_set)



e = Two(1, 3434, 'name')
o = One(1, 3)


