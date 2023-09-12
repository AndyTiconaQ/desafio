def segundo_a_minutos(segundo):
    return segundo /60

def minutos_a_horas(minutos):
    return minutos /60

if __name__=="__main__":
    segundos= 3600
    minutos= segundo_a_minutos(segundos)
    horas= minutos_a_horas(minutos)
    print(f"{segundos} segundos equivalente a {minutos} minutos ")
    print(f"{minutos} minutos son equivalente a {horas} horas ")