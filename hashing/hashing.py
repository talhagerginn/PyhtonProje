import hashlib as hasher
from Crypto.Cipher import DES
import re
import random
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import binascii
class dilKontrol:
    def __init__(self,kelime):
        self.kelime=kelime
    def cumleAyir(self):
        l=self.kelime.split(".")
        print(l)
        #cumle sayısını geri döndürecek
    def cumleSayisi(self):
        x=len(self.kelime.split("."))-1
        print(f"Girilen cumle sayisi: {x}")
    def kelimeAyir(self):
        l=self.kelime.split(" ")
        print(l)
        return  l
    def kelimeSayisi(self):
        y=len(self.kelime.split(" "))
        print(f'Girilen kelime sayisi: {y}')
    def sesliHarf(self):
        i=0
        sesli = "aeıioöuü"
        for x in self.kelime:
            if x in sesli:
                i += 1
        print("Girdiginiz cümle de bulunan sesli harf sayısı: ",i)
        return i
    def unluUyumu(self):
        kalin_unluler = list("aıou")  # veya ['a', 'ı', 'o', 'u']
        ince_unluler = list("eiöü")  # veya ['e', 'i', 'ö', 'ü']
        if (sum(self.kelime.count(kalin) for kalin in kalin_unluler)) != 0 and (sum(self.kelime.count(ince) for ince in ince_unluler)) != 0:
            print(f"'{self.kelime.capitalize()}' Büyük Ünlü Uyumuna Uymaz.")
        else:
            print(f"'{self.kelime.capitalize()}' Büyük Ünlü Uyumuna Uyar.")
def check(kelime):#türkçe uygunluk kontrolu
    yabanci_karakterler='qQwWxX'
    for i in a:
        if i in yabanci_karakterler:
            raise Exception('Kelimeler yabanci karakter içeremez')


class sifrelemeYontemleri:
    def __init__(self,metin):
        self.metin=metin
#2.şifreleme yöntemi
    def sha256(self):
        sifreleyici=hasher.sha256()
        sifreleyici.update(self.metin.encode("utf-8"))
        hash=sifreleyici.hexdigest()
        print(hash)

    def md5hashislemi(self):
        d = hasher.md5()
        d.update(self.metin.encode('utf-8'))
        return d.hexdigest()
#3.şifrelene yöntemi blake2
    def blake2b(self):
        gfg = hasher.blake2b()
        gfg.update(self.metin.encode("utf-8"))
        print('Blake2b Sifreleme Sonucu: ',gfg.digest())

#4.yöntemi sha384
    def sha384(self):

        sifreleyici=hasher.sha384()
        metin="deneme notu"
        sifreleyici.update(metin.encode("utf-8"))
        hash=sifreleyici.hexdigest()
        print("SHA 384 Sifreleme Sonucu: ",hash)
#5.şifre
    def sha512(self):
        sifreleyici=hasher.sha3_512()
        metin="deneme notu"
        sifreleyici.update(metin.encode("utf-8"))
        hash=sifreleyici.hexdigest()
        print("SHA 512 Sifreleme Sonucu",hash)

    def sezar(self):
        sifre=""
        for k in self.metin:
            sifre=sifre+chr(ord(k)+5^2)
        print("Sezar Sifreleme Sonucu:",sifre)
    def sha256(self):
        hashObject = SHA256.new()
        hashObject.update(b'self.kelime')
        print(hashObject.hexdigest())

    def rsa(self):
#RSA keyleri oluşturuyoruz(1024 bit) ve yazdırdık
#Görmek için yazdırdık yazdırmasakta olur.
        keyPair = RSA.generate(3072)

        pubKey = keyPair.publickey()
        print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
        pubKeyPEM = pubKey.exportKey()
        print(pubKeyPEM.decode('ascii'))

        print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
        privKeyPEM = keyPair.exportKey()
        print(privKeyPEM.decode('ascii'))
#Şifreleme işlemini burda yapıyoruz
        msg = b'self.metin'
        sifreleme = PKCS1_OAEP.new(pubKey)
        sifrelendi = sifreleme.encrypt(msg)

a =input("cumle gir: ")
for x in a:
    try:
        check(a)
    except ValueError as err:
        print(err)
    continue

a1=dilKontrol(a)
a1.kelimeAyir()
a1.cumleAyir()
a1.cumleSayisi()
a1.kelimeSayisi()
a1.sesliHarf()
a1.unluUyumu()

a2=sifrelemeYontemleri(a)
x=int(input("\n1-MD5 Şifreleme\n2-SHA 384 Şİfreleme\n3-SHA 512 Şifreleme\n4-Blake2b Şifreleme\n5-Sezar Şifreleme\n6-SHA 256 Şifreleme\n7-DES Şifreleme\n8-RSA Şifreleme\nŞifreleme yapmak istediğiniz yöntemi seçiniz:\n"))
if x==1:
    print("Hashing Sonucu: ",a2.md5hashislemi())
elif x==2:
    a2.sha384()
elif x==3:
    a2.sha512()
elif x==4:
    a2.blake2b()
elif x==5:
    a2.sezar()
elif x==6:
    a2.sha256()
elif x==7:
    a2.pad()
elif x==8:
    a2.rsa()
else:
    print("Hatali Seçim Yaptınız!")
print(dir(sifrelemeYontemleri))
class Help():
    def __init__(self):
        x=int(input("\n1-dilKontrol\n2-sifrelemeYontemleri\nBilgi almak istediğiniz sınıfı seçiniz...\n"))
        if x == 1:
            print("dilKontrol adlı sınıfın fonksiyonları:\n",dir(dilKontrol))
        elif x == 2:
            print("sifrelemeYontemleri adlı sınıfın fonksiyonları:\n",dir(sifrelemeYontemleri))
        else:
            print("Hatalı Seçim Yaptınız!")
    def bilgi(self):
        print("dilKontrol sınıfı fonksiyonrından\n1-cumleAyir fonksiyonu girdiğiniz veriyi . işaretine göre cümleleri tespit eder."
              "\n2-cumleSayisi fonksiyonu string tipinde girdiğiniz verinin cümle sayisini döndürür\n3-kelimeAyir fonksiyonu string tipinde girdiğiniz verideki kelimeleri tespit eder\n"
              "4-kelimeSayisi fonksiyonu string tipinde  girdiğiniz verinin kelime sayisini döndürür.\n5-sesliHarf fonksiyonu string tipinde  girdiğiniz verideki sesli harfleri tespit ederek"
              "sayisini geri döndürür.\n6-unluUyumu fonksiyonu string tipinde  girdiğiniz verinin bütün karakterlerini gezerek büyük ünlü uyumu olup olmadığına bakar\n"
              "6-Check fonksiyonu girdiğiniz verinin uygunluğunu kontrol eder."
              )#kodla çağırmak için a2. yazarak istediğiniz fonksiyona ulaşabilirsiniz

        x=int(input("Denemek istediğiniz fonksiyonu seçiniz...Devam etmek için 0(sıfır)'a basınız..."))
        if x ==1 :
            a1.cumleAyir()
        elif x == 2:
            a1.cumleSayisi()
        elif x==3:
            a1.kelimeAyir()
        elif x == 4:
            a1.kelimeSayisi()
        elif x == 5:
            a1.sesliHarf()
        elif x== 6:
            a1.unluUyumu()
        elif x == 0:
            pass
        else:
            print("Hatalı Giriş!")

    def bilgi2(self):
        print(
            "sifrelemeYontemleri sınıfı fonksiyonlarından \n1-MD5\n2-SHA256\n3-SHA384\n4-SHA512\n5-blake2b  fonskiyonları Hash Şifreleme Yöntemidir.\n"
            "\n6-sezar fonksiyonu ilkel şifreleme yöntemidir.\n7-RSA fonksiyonu Asimetrik şifreleme algoritmasıdır...")
        # kodla çağırmak için a1. yazarak istediğiniz fonksiyona ulaşabilirsiniz
        y = int(input("Denemek istediğiniz fonksiyonu seçiniz... Yoksa 0(sıfır)'a basınız..."))
        if y == 1:
            a2.md5hashislemi()
        elif y == 2:
            a2.sha256()
        elif y == 3:
            a2.sha384()
        elif y == 4:
            a2.sha512()
        elif y == 5:
            a2.blake2b()
        elif y == 6:
            a2.sezar()
        elif y == 7:
            a2.rsa()
        elif y == 0:
            pass
        else:
            print("Hatalı giriş!")

a3=Help()
a3.bilgi()
a3.bilgi2()
#GRUP ÜYELERİ TALHA GERGİN/ROJİN TEMEL/BESTE