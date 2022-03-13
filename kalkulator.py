while True :
    print ("KALKULATOR SEDERHANA".center(50,' '))
    print ("="*50)
    print ('1. perkalian')
    print ('2. pembagian')
    print ('3. penjumlahan')
    print ('4. pengurangan')
    print ('0. exit')
    operasi = int(input("masukan nomor pilihan operasi : "))
    while operasi >4 or operasi<0 :
        print ('silahkan masukan angka yang ada pada menu.')
        operasi = int(input("masukan nomor pilihan operasi : "))
        print ('')
    if operasi == 0 :
        break
    else :
        a = int(input("masukan nilai a : "))
        b = int(input("masukan nilai b : "))
        if operasi == 1:
            perkalian = a*b
            print (a,"*",b," = ",perkalian)
        elif operasi == 2:
            pembagian = a/b
            print (a,"/",b," = ",pembagian)
        elif operasi == 3:
            penjumlahan = a+b
            print (a,"+",b," = ",penjumlahan)
        elif operasi == 4:
            pengurangan = a-b
            print (a,"-",b," = ",pengurangan)
