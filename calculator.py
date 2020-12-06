def calculate (a,b,operacja):
    if operacja == "+":
        return a + b

    if operacja == '-':
        return a-b

    if operacja == '*':
        return a*b

    if operacja == '/':
        return a/b

    if operacja == '%':
        return a%b

    if operacja == '^':
        return a**b

    return 0

def str_calculator (a,b,operacja):
    if operacja == "concat":
        return a + b

    if operacja == "contain":
        idx = a.find(b)
        if idx != -1: return 1
        else:  return idx

    if operacja == "enda":
        return b.endswith(a)

    if operacja == "startb":
        return a.startswith(b)
    return -1
