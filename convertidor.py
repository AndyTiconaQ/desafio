import temperatura
import masa
import tiempo

def convertidor_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen =="celsius" and unidad_destino =="fahrenheit":
        return temperatura.celsius_a_fahrenheit(valor)
    if unidad_origen =="celsius" and unidad_destino =="kelvin":
        return temperatura.celsius_a_kelvin(valor)

def convertir_masa(valor,unidad_origen, unidad_destino):
    if unidad_origen =="kilogramos" and unidad_destino =="gramos":
        return masa.kilogramos_a_gramos(valor)
    if unidad_origen =="kilogramos" and unidad_destino =="tolenadas":
        return masa.kilogramos_a_tolenadas(valor)

def convertir_tiempo(valor,unidad_origen, unidad_destino):
    if unidad_origen =="segundos" and unidad_destino =="minutos":
        return tiempo.segundo_a_minutos(valor)
    if unidad_origen =="minutos" and unidad_destino =="horas":
        return tiempo.minutos_a_horas(valor)

if __name__=="__main__":
    valor= 20
    unidad_origen="celsius"
    unidad_destino="fahrenheit"
    resultado= convertidor_temperatura(valor,unidad_origen, unidad_destino)
    print(f"{valor} grados {unidad_origen} equivale a {resultado} grados {unidad_destino}")

    unidad_origen="celsius"
    unidad_destino="kelvin"
    resultado= convertidor_temperatura(valor,unidad_origen, unidad_destino)
    print(f"{valor} grados {unidad_origen} equivale a {resultado} grados {unidad_destino}")

    valor=100
    unidad_origen="kilogramos"
    unidad_destino="gramos"
    resultado= convertir_masa(valor,unidad_origen, unidad_destino)
    print(f"{valor} {unidad_origen} equivale a {resultado} {unidad_destino}")

    unidad_origen="kilogramos"
    unidad_destino="tolenadas"
    resultado= convertir_masa(valor,unidad_origen, unidad_destino)
    print(f"{valor} {unidad_origen} equivale a {resultado} {unidad_destino}")

    valor=3600
    unidad_origen="segundos"
    unidad_destino="minutos"
    resultado= convertir_tiempo(valor,unidad_origen, unidad_destino)
    print(f"{valor} {unidad_origen} equivale a {resultado} {unidad_destino}")

    unidad_origen="minutos"
    unidad_destino="horas"
    resultado= convertir_tiempo(valor,unidad_origen, unidad_destino)
    print(f"{valor} {unidad_origen} equivale a {resultado} {unidad_destino}")