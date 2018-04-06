#
# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1

#-----------------------------------------------------------------------------

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#-----------------------------------------------------------------------------

class V2:
    # Delete the pass statement below and insert your own code
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def add(self, v):
        return V2(self.x + v.x, self.y + v.y)
    
    def mul(self, n):
        return V2(self.x * n, self.y * n)

    def __add__(self, v):
        return self.add(v)

    def __str__(self):
        return 'V2[' + str(self.x) + ', ' + str(self.y) + ']'
    
#-----------------------------------------------------------------------------

class Polynomial:
    # Delete the pass statement below and insert your own code
    def __init__(self, li):
        self.li = li

    def add(self, p2):
        max_len = max(len(self.li), len(p2.li))
        result = []
        for i in range(1, max_len + 1):
            a = 0
            b = 0
            if len(self.li) >= i:
                a = self.li[-i]
            if len(p2.li) >= i:
                b = p2.li[-i]
            result.insert(0, a + b)
        return Polynomial(result)

    def mul(self, p2):
        p1_len = len(self.li)
        p2_len = len(p2.li)
        po_li = []
        for i in range(p2_len):
            print('i:' + str(i))
            li = []
            for j in range(p1_len + p2_len - 1):
                if j < i or j >= p1_len + i:
                    li.append(0)
                else:
                    li.append(p2.li[i] * self.li[j - i])
            po_li.append(Polynomial(li))

        result = po_li[0]
        for i in range(1, len(po_li)):
            result += po_li[i]
        return result

    def __add__(self, p2):
        return self.add(p2)

    def __call__(self, v):
        result = 0
        for idx, value in enumerate(self.li):
            result += value * v ** (len(self.li) - 1 - idx)
        return '{:.1f}'.format(result)

    def __str__(self):
        if len(self.li) > 0:
            result = []
            fmt = '{:.3f}'
            for idx, val in enumerate(self.li):
                if idx == len(self.li) - 1:
                    result.append(fmt.format(val))
                elif idx == len(self.li) - 2:
                    result.append(fmt.format(val) + ' z')
                else:
                    result.append(fmt.format(val) + ' z**' + str(len(self.li) - 1 - idx))
            return ' + '.join(result)
