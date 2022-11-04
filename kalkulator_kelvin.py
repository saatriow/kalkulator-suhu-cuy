elif (pil==4):
    suhu= float(input("Masukkan Suhu KKelvin awal : "))
    pil2 = int(input("ubah ke : \n1. Celcius \n2. Fahrenhait \n3. reamur\n"))
    if (pil2==1):
        print (suhu, "Kelvin = ", suhu - 273 ,"Celcius")
    elif(pil2==2):
        pprint(suhu, "Kelvin = ", (9/5*(suhu-273)+32) ,"Fahhrenhait")
    elif(pil2==3):
        print(suhu, "kelvin = ", (4/5*(suhu-273)) ,"reamur")
    else:
        print("Tidakk valid")
else:
    print("tidak valid")
