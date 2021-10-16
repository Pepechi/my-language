class INTEGER:
    def __init__(self, value_, name_):
        self.value = value_
        self.name = name_
        self.printvalue = "INT " + name_

class STR:
    def __init__(self, value_, name_):
        self.value = value_
        self.name = name_
        self.printvalue = "STR " + name_

def where(input, what):
    for i in range(len(input)):
        if input[i] == what:
            w = i
    return w

def translate(Input):
    Done = False
    arr = []
    c = 0
    
    while not Done:
        if Input[c] == ";":
            break
        # Defining an integer?
        if Input[c:c+3] == "int":
            # Getting the name of the integer
            whr = where(Input, "=")
            intname = Input[c+4:whr-1]
            # Getting the value of the integer*
            intvalue = Input[whr+1:len(Input)-1]
            arr.append("add")
            arr.append(INTEGER(intvalue, intname))
        # print(Input[c:c+3])
        c+=1
    return arr

def res(Input):
    output = translate(Input)
    return output