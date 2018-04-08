import lib601.sm as sm

class Accumulator(sm.SM):

    startState = 0

    def getNextValues(self, state, inp):
        return state + inp, state + inp

a = Accumulator()
a.start()
print(a.step(3))
print(a.step(4))
print(a.step(-2))