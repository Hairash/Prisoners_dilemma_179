def abrikos_bot(*args):
    s = str(args)
    h = hash(s)
    if h%8 == 0:
        return False
    return True
