suhu= float(input("Masukkan Suhu Awal Reamur yang akan di Konversi : "))
    pil2 = int(input("ubah ke mana ya inii : \n1. Celcius \n2. Fahrenheit \n3. Kelvin\n"))
    if (pil2==1):
        print (suhu, "Reamur = ", (5/4*suhu) ,"Celcius")
    elif(pil2==2):
        print(suhu, "Reamur = ", (9/4*suhu) + 32 ,"Fahrenheit")
    elif(pil2==3):
        print(suhu, "Reamur = ", (5/4*suhu) + 273 ,"Kelvin")
    else:
        print("Silahkan coba ulang, data Tidak valid")
