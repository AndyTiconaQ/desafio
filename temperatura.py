def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

if __name__=="__main__":
    celsius =25
    fahrenheit= celsius_a_fahrenheit(celsius)
    kelvin= celsius_a_kelvin(celsius)
    print(f"{celsius} grados celcius son equivalente a {fahrenheit} grados fahrenheit")
    print(f"{celsius} grados celcius son equivalente a {kelvin} grados kelvin")
