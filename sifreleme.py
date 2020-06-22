
import random as rd
import string



#import string ile ASCII Uppercase aldım.

#asal sayılardan oluşarak harfleri listeye ekledim.

def sifrele(girdi):
    karakter = len(girdi)
    anahtar = {"a": 3, "b": 5, "c": 7, "d": 11, "e": 13, "f": 17, "g": 19, "h": 23, "ı": 31, "i": 37, "j": 41, "k": 43,
               "l": 47, "m": 53, "n": 59, "o": 61, "p": 71, "r": 73, "s": 79, "t": 83, "u": 89, "v": 97, "y": 101,
               "z":107, " ":109}
    kar_anah = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "J",10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "R", 17: "S", 18: "T",19: "U", 20: "V", 21: "Y", 22: "Z"}
    thash = 1
    thash2 = ""
    a = 0
    deg = []

    rast = rd.choice(string.ascii_uppercase) + kar_anah[karakter] + rd.choice(
        string.ascii_uppercase)
    rast2 = ''.join(rd.choices(string.ascii_uppercase, k=3))

    for i in girdi:
        thash *= anahtar[i]
        deg.append(anahtar[i])

#anahtar[i] 'nin görevi örneğin A girince 3 veriyor.

#deg = Anahtarların değeri yani asal sayılar


    ceg = deg[::]

#Bunları birbirine eşitledim ki iki liste olsun.


    while deg != []:
        maks = max(deg)
        if ceg.count(maks) > 1:
            try:
                m_in = ceg.index(maks, a) + 1
            except:
                a = 0
                m_in = ceg.index(maks, a) + 1
            a = m_in
        else:
            m_in = ceg.index(maks) + 1

        thash2 += str(m_in)
        deg.remove(maks)

#try - except kullanmanın amacı bir hata veriyor o hatadan kaçsın diye.

#while döngüsü ile Asal sayıların maksimum değerini alacağım.


    return rast2 + thash2[0:(len(thash2) // 2) + 1] + str(thash) + thash2[(len(thash2) // 2) + 1:] + str(rast)


def sifre_coz(girdi):
    anahtar = {"a": 3, "b": 5, "c": 7, "d": 11, "e": 13, "f": 17, "g": 19, "h": 23, "ı": 31, "i": 37, "j": 41, "k": 43,
               "l": 47, "m": 53, "n": 59, "o": 61, "p": 71, "r": 73, "s": 79, "t": 83, "u": 89, "v": 97, "y": 101,
               "z":107, " ":109}
    kar_anah = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "J",10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "R", 17: "S", 18: "T",19: "U", 20: "V", 21: "Y", 22: "Z"}


    key_anahtar = list(anahtar.keys())
    val_anahtar = list(anahtar.values())

    key_kar = list(kar_anah.keys())
    val_kar = list(kar_anah.values())

    karakter = int(key_kar[val_kar.index(girdi[-2])])

    c = girdi[3:(3 + karakter // 2) + 1]
    d = girdi[-4:-3 + (-karakter // 2):-1]
    d = d[::-1]
    thash = int(girdi[4 + karakter // 2:len(girdi) + (-3 + (-karakter // 2) + 1)])
    thash2 = c + d
    deger = []
    cozum = {}
    cikti = ""
    for i in val_anahtar:
        while thash % int(i) == 0:
            deger.append(int(i))
            thash /= int(i)
    for t in thash2:
        cozum[int(t)] = max(deger)
        deger.remove(max(deger))

    for f in range(1, karakter + 1):
        cikti += key_anahtar[val_anahtar.index(cozum[f])]
    return cikti

x = input("Ne Şifrelensin?: ")
print(sifrele(x))

y = input("Çözülecek Şifre?: ")
print(sifre_coz(y))
