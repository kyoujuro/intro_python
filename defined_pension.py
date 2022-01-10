class Present_value:
    def __init__(self, an, i):
        self.an = an
        self.i = i

    def risoku(an, sn):
        return 1 / an + 1 / sn
    def genka(self):
        return self.an * (1 + self.i)