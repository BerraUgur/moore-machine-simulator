import os
sonluDurumlar=[]
girdiDizisi=["a","b"]
olasiCikti=[0,1]

def yeniGiris(elemanSayisi):
    sonluDurumlar.clear()
    girisCikis= [[0 for x in range(4)] for y in range(elemanSayisi)]
    for i in range(elemanSayisi): #sonlu durumlar kümesi oluşturuldu
        ek="q"+str(i)
        sonluDurumlar.append(ek)
    for i in range(elemanSayisi):
        index=0
        girisCikis[i][index]=sonluDurumlar[i]
        for j in girdiDizisi:
            clear()
            while True: #Durumlar arası geçiş alındı
                if i!=0:
                    tablo(girisCikis,girdiDizisi,i)
                kontrol=0
                print("\n",sonluDurumlar[i],"Durum Geçişi")
                say=1
                for k in sonluDurumlar:
                    print(say,"- ",sonluDurumlar[i],">>",k)
                    say+=1
                try:
                    giris=int(input("\n"+j+" girişindeki geçiş: "))
                    for l in range(1,say):
                        if giris==l:
                            kontrol=1
                            break
                    if kontrol==1:
                        index+=1
                        girisCikis[i][index]=sonluDurumlar[giris-1]
                        break
                    else:
                        input("Yanlış değer girdiniz\n")
                        clear()    
                except ValueError:
                    input("Hatalı değer girdiniz\n")
                    clear()
                    continue
        index+=1
        kontrol=0
        while True: #Olası çıktı verileri alındı
            try:
                clear()
                if i!=0:
                    tablo(girisCikis,girdiDizisi,i)
                cikis=int(input(sonluDurumlar[i]+" durumu için cikis değeri : "))
                for j in olasiCikti:
                    if cikis==j:
                        kontrol=1
                if kontrol==1:
                    girisCikis[i][index]=cikis
                    break
                else:
                    print(olasiCikti," seçeneklerinden birini giriniz")
            except ValueError:
                continue
        tablo(girisCikis,girdiDizisi,i+1)
    return girisCikis

def tablo(giris, girdi,elemanSayisi):
    clear()
    print("_________________________________________________________________________")
    print("|                  Transition Table",end="                  ")
    print("|   Output Table    |")
    print("|____________________________________________________|___________________|")
    print("| Old State |",end="    ")
    for i in girdi:
        print("After input ",i,end="    ")
    print("| Character printed |")
    print("|-----------|----------------------------------------|-------------------|")
    for i in range(elemanSayisi):  #Sonlu durumlar kümesinin eleman sayısı kadar satır oluşturuldu ve veriler tabloda gösterildi
        print("|",end="    ")
        for j in range(4):
            if j==0:
                print(giris[i][j],end="     |          ")
            elif j==1:
                print(giris[i][j],end="                ")
            elif j==2:
                print(giris[i][j],end="          ")
            else:
                print("|        ",giris[i][j],"        |")
    print("|___________|________________________________________|___________________|")

def moore(inputString,girisCikis,elemansayisi): #bilgilerini tablo halinde ekrana göstermesi için oluşturuldu
    inputCount=len(inputString)
    aktifDurum="q0"
    durum=[]
    output=[]
    durum.append(aktifDurum)
    output.append(0)
    for i in range(inputCount): #alınan string'e göre makineden kontrol ve düzenleme işlemi
        kontrol=0
        for j in range(len(girdiDizisi)):
            if inputString[i]==girdiDizisi[j]:
                ind=j+1
                for k in range(elemanSayisi):
                    if girisCikis[k][0]==aktifDurum:
                        aktifDurum=girisCikis[k][ind]
                        durum.append(aktifDurum)
                        for l in range(elemanSayisi):
                            if girisCikis[l][0]==aktifDurum:
                                output.append(girisCikis[l][3])
                                break
                        kontrol=1
                        break
            if kontrol==1:
                break
    print("____________________",end="") #tablolama işleminde girilen stringde girdi dizisinde bulunmayan karakterler yok sayıldı
    for i in range(inputCount):
        for j in girdiDizisi:
            if inputString[i]==j:
                print("___",end="")
    print("\n|Input String",end="  |    ")
    for i in range(inputCount):
        for j in girdiDizisi:
            if inputString[i]==j:
                print(inputString[i],end="  ")
    print("|\n|State",end="         |")
    for i in durum:
        print(i,end=" ")
    print(" |\n|Output",end="        | ")
    for i in output:
        print(i,end="  ")
    print("|\n|______________",end="|____")
    for i in range(inputCount):
        for j in girdiDizisi:
            if inputString[i]==j:
                print("___",end="")
    print("|")

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

clear()
while True:                         
    clear()
    print("1. Moore Makinesi")
    print("0. Çıkış")
    try:
        secim= int(input("\nMenüden seçim yapın: "))
        if secim==0:
            clear()
            input("Program sonlandırıldı")
            break
        elif secim==1:
            clear()
            elemanSayisi=int(input("Sonlu durumlar kümesinin eleman sayısını giriniz: "))
            giris=yeniGiris(elemanSayisi)
            inputStr=input("\nGiriş stringi: ")
            moore(inputStr,giris,elemanSayisi)
            input("\n\nAna menüye dönmek için Enter'a basınız")
        else:
            clear()
            print("Hatalı Seçim yaptınız")
            input("\n\nAna menüye dönmek için Enter'a basınız")
    except ValueError:
        clear()
        print("Hatalı Seçim yaptınız")
        input("\n\nAna menüye dönmek için Enter'a basınız")
        continue