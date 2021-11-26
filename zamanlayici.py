import time
from pymsgbox import *
cevap=str(input("Dakika saydirmak ister misiniz? istiyorsan evet yaz:"))
def saydir():
    a=int(input("Kaç dakika geri sayayım:"))
    b=a*60
    sayilan_sure=a*60
    while True:
        b-=1
        time.sleep(1)
        print(b)
        if(b==0):
            alert(text='süre bitti',title='Sayac', button='Tamam')
            cevap2=str(input("Tekrar saydirmak istiyor musun istiyorsan evet yaz:"))
            if(cevap2=="evet"):
                saydir()
            else:
                print("Çıkış yaptım")
                break
if(cevap=="evet"):
    saydir()
else:
    print("Cikis yaptım senin için")
    



