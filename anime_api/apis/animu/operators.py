class AND:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return ','.join(str(arg) for arg in self.args)

class OR:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return '|'.join(str(arg) for arg in self.args)
