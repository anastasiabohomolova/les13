class One:
    def __init__(self, *args):
        self.args = args


class Two(One):
    def __init__(self, *args):
        self.args = args




e = Two(12, 343, 56, 'erere', 'fdfdf', [323234, 454, 'gfgfg'])
o = One(1, 3)
print(e.args)
print(o.args)









