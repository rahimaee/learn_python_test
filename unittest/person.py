class Pesron:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return F"{self.fname} {self.lname}"

    def email(self):
        return F'{self.fullname()}@gmail.com'.replace(" ", '')


p1 = Pesron('mohammad', 'rahimaee')
print(p1.email())
print(p1.fullname())
