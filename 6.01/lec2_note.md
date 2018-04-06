### functional thinking
    def apply(opsList, arg):
        if len(opsList) == 0:
            return arg
        else:
            return apply(opsList[1:], opsList[0](arg))

    def addLevel(opsList, fctList):
        return [x + [y] for y in fctList for x in opsList]

    def findAnswer(opsList, fctList, init, goal):
        for opList in opsList:
            if apply(opList, init) == goal:
                return opList
        return findAnswer(addLevel(opsList, fctList), fctList, init, goal)

    def inc(n):
        return n + 1
    
    def square(n):
        return n * n

    findAnswer([[inc]], [inc, square], 1, 100)