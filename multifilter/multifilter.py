class MultiFilter:

    def judge_half(self, pos, neg):
	# допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

        if self.pos >= self.neg:
            return True
        else:
            return False

    def judge_any(self, pos, neg):
	# допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

        if self.pos >= 1:
            return True
        else:
            return False

    def judge_all(self, pos, neg):
	# допускает элемент, если его допускают все функции (neg == 0)
        if self.neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.judge = judge
        self.funcs = funcs
        self.pos = 0
        self.neg = 0

    def __iter__(self):
        for i in self.iterable:         
            self.pos, self.neg = 0, 0   
            for f in self.funcs:        
                if f(i):                
                    self.pos += 1      
                else:                   
                    self.neg += 1      
            print(self.pos, self.neg)
            if self.judge(self, self.neg, self.neg):
                yield i


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]
print(list(MultiFilter(a, mul2, mul3, mul5)))
