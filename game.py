def func1(history, n, table):
    return True

def func2(history, n, table):
    return False

table = [[(0, 0), (3, -1)], [(-1, 3), (2, 2)]]

def match(f1, f2, n):
    history = []
    
    for i in range(n):
        res1 = f1(history, 0, table)
        res2 = f2(history, 1, table)
        history.append((res1, res2))

    print(history)

    
