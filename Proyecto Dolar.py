#PROYECTO DE SIMULACION DEL DOLAR MONITOR 
#INTEGRANTES ARMANDO SERRA Y YONKEINER BRAVO
#ING.EN INFORMATICA SECCION "1"
Airtmlnc = float(input("ingrese el valor de @Airtmlnc:"))
localBitcoins = float(input("ingrese el valor de @localBitcoins:"))
Yadio_io = float(input("ingrese el valor de Yadio_io:"))
usdtBnbzla = float(input("ingrese el valor de usdtBnbzla:"))
Mkambio = float(input("ingrese el valor de Mkambio:"))
CambiosRya = float(input("ingrese el valor de CambiosRya:"))
HolaReserve = float(input("ingrese el valor de HolaReserve:"))

suma = Airtmlnc + localBitcoins + Yadio_io + usdtBnbzla + Mkambio + CambiosRya 
+ HolaReserve 
promedio = suma/7
tasa = round(promedio,2)
print("")
print("")

print("\t22/11/2022\t09:00 AM")
print(f"\tPROMEDIO Bs.{tasa} ")
print("Unica cuenta oficial\t@Enpararelo3")

print("")
print(f"@Airtmlnc               Bs.{Airtmlnc} ")
print("")
print(f"@localBitcoins          Bs.{localBitcoins} ")
print("")
print(f"@Yadio_io               Bs.{Yadio_io} ")
print("")
print(f"@usdtBnbzla             Bs.{usdtBnbzla} ")
print("")
print(f"@Mkambio                Bs.{Mkambio} ")
print("")
print(f"@CambiosRya             Bs.{CambiosRya}")
print("")
print(f"@HolaReserve            Bs.{HolaReserve} ")
print("")
while True:
    print(" ")
    print(f"\tTasa De Cambio {tasa} ")
    print("1.Convertir de Dolares a Bolivares")
    print("2.Convertir de Bolivares a Dolares")
    print("3.Salir")
    opcion = int(input("INGRESE UNA OPCION DE MENU:."))
    
    if opcion == 1:
        dolares = float(input("Ingrese la cantidad de dolares a cambiar:."))
        cambioDolares = dolares * tasa
        print(f"Cambiar {dolares} Dolares a una tasa de {tasa} Bs Es un total de: {cambioDolares} ")
    elif opcion == 2:
        bolivares = float(input("Ingrese la cantidad de bolivares a cambiar"))
        cambioBolivares = bolivares * tasa
        print(f"Cambiar {bolivares} Bs a una tasa de {tasa} Dolares Es un total de:{cambioBolivares} ")

    elif opcion == 3:
        break    
                

















