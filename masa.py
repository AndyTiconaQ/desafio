def kilogramos_a_gramos(kilogramos):
    return kilogramos *1000

def kilogramos_a_tolenadas(kilogramos):
    return kilogramos /1000

if __name__=="__main__":
    kilogramos= 2.5
    gramos= kilogramos_a_gramos(kilogramos)
    tolenadas= kilogramos_a_tolenadas(kilogramos)
    print(f"{kilogramos} kilogramos son equivalente a {gramos} grados ")
    print(f"{kilogramos} kilogramos son equivalente a {tolenadas} tolenadas ")