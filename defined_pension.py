class Present_value:
    def __init__(self, an, i, v):
        self.an = an
        self.i = i
        self.v = v
    def risoku(an, sn):
        return 1 / an + 1 / sn
    def genka(self):
        return self.an * (1 + self.i)
    def kimatsu_genka(self):
        return self.genka(self) * self.v