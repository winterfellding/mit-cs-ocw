### functional thinking
```python
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
```

### recursion

```python
def pow(b, n):
    if n == 0:
        return 1
    return b * pow(n - 1)

# faster version
def pow(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(b, n/2) ** 2
    else:
        return b * pow(b, n - 1)

def hanoi(n, A, B, C):
    if n == 1:
        print('Move from ' + A + ' to ' + B)
    else:
        hanoi(n - 1, A, C, B)
        hanoi(1, A, B, C)
        hanoi(n - 1, C, B, A)
hanoi(2, 'A', 'B', 'C')
```

### State Machine

finite-state machine    => state machine
infinite-state machine  => stack machine
Computability_theory_(computer_science) wikipedia