# bu generator ning qisqacha codi
class Range:
    """
    endi class yaratamiz
    """
    def __init__(self, start, stop=None, step=1):
        # bu yerda biz init qilib start stop step object qabul qilibolyammiz
        if stop is None:
            """
            va bu yerda shart orqali objectni o'zlashtiryapmiz"""
            self.stop = start
            self.start = -step
            self.step = step
        else:
            """ bu yerda shartsiz objectni o'zlashtiryapmiz """
            self.start = start - step
            self.stop = stop
            self.step = step

    def __iter__(self):
        # buyerdaa itereble ishlatyapmiz
        return self

    def __next__(self):
        if self.start > self.stop and self.step > 0:
            raise StopIteration

        elif self.start > self.stop and self.step < 0:
            self.start += self.step
            if self.stop >= self.start:
                raise StopIteration
            return self.start

        elif self.start < self.stop and self.step > 0:
            self.start += self.step
            if self.start >= self.stop:
                raise StopIteration
            return self.start

        elif self.start < self.stop and self.step < 0:
            raise StopIteration


for i in Range(1, 25, -2):
    print(i)


