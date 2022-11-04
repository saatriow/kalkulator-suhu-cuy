print("==========KALKULATOR SUHU GIS 2==========")
print("Pilih suhu yang ingin dirubah")
pil = int(input("1. Celcius \n2. Fahrenhait \n3. Reamur \n4. Kelvin \n"))
if (pil == 1):
    suhu= float(input("Masukkan Suhu Celcius awal : "))
    pil2 = int(input("ubah celcius ke : \n1. Fahrenhait \n2. Reamur \n3. Kelvin \n"))
    if (pil2==1):
        print(suhu, "celcius = ", (9/5*suhu)+32 ,"Fahrenhait")
    elif(pil2==2):
        print(suhu, "celcius = ", (4/5*suhu) ,"Reamur")
    elif(pil2==3):
        print(suhu, "celcius = ", suhu + 273 ,"Kelvin")
    else:
        print("Tidak valid")
elif (pil == 2):
    suhu= float(input("Masukkan Suhu Fahrenhait awal : "))
    pil2 = int(input("ubah ke : \n1. Celcius \n2. Reamur \n3. Kelvin\n"))
    if (pil2==1):
        print(suhu, "Fahrenhait = ", (5/9*(suhu-32)) ,"Celcius")
    elif(pil2==2):
        print(suhu, "Fahrenhait = ", (4/9*(suhu-32)) ,"Reamur")
    elif(pil2==3):
        print(suhu, "Fahrenhait = ", (5/9*(suhu-32) + 273) ,"Kelvin")
    else:
        print("Tidak valid")
        
    elif (pil==4):
    suhu= float(input("Masukkan Suhu Kelvin awal : "))
    pil2 = int(input("ubah ke : \n1. Celcius \n2. Fahrenhait \n3. Reamur\n"))
    if (pil2==1):
        print (suhu, "Kelvin = ", suhu - 273 ,"Celcius")
    elif(pil2==2):
        print(suhu, "Kelvin = ", (9/5*(suhu-273)+32) ,"Fahrenhait")
    elif(pil2==3):
        print(suhu, "kelvin = ", (4/5*(suhu-273)) ,"Reamur")
    else:
        print("Tidak valid")
    else:
        print("tidak valid")
