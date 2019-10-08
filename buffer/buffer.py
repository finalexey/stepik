class Buffer:
    def __init__(self, lst=[]):
        self.lst = lst

    def adding(self, l):
        print(sum(self.lst[:5]))
        del self.lst[:5]

    def add(self, *a):
        self.lst.extend(a)
        while len(self.lst) >= 5:
            self.adding(self.lst)

    def get_current_part(self):
        return self.lst

