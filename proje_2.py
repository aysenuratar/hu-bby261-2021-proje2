#Arayüz paketinin eklenmesi
from tkinter import *
from random import randint

acilir_pencere = Tk()
acilir_pencere.title('Sayısal Loto')
acilir_pencere.configure(bg="light blue")
acilir_pencere.geometry("900x900")

baslik = Label(acilir_pencere, text="Sayısal loto uygulamasına hoş geldiniz! Günün şanslı rakamlarını öğrenmek ister misiniz?")
baslik.config(font=("Times New Roman", 17), fg="black", bg="pink")
baslik.grid()

def sayisal_loto():
  i = 0
  secilenler = [0, 0, 0, 0, 0, 0]
  for rastgele in secilenler:
    while i < len(secilenler):
      secilen = randint(1, 49)
      if secilen not in secilenler:
        secilenler[i] = secilen
        i += 1
    sirali_rakamlar = sorted(secilenler)
    i = 0

    rakamlar = Label(acilir_pencere, text=sirali_rakamlar)
    rakamlar.config(font=("Times New Roman", 15))
    rakamlar.grid(row=10, column=10)

buton = Button(acilir_pencere, text="Şanslı rakamları listele", command=sayisal_loto)
buton.config(font=("Times New Roman", 15), fg="black", bg="white")
buton.grid(column=0, row=10)
buton.grid()

def yardim():
    bilgilendirme ="Hoş geldiniz. Size nasıl yardımcı olabiliriz? 1.Şanslı rakamları listele butonuna tıkladığınızda rakamları göreceksniz. 2. Sonlandır butonuna tıkladığınızda sayısal loto uygulamasından ayrılacaksınız."
    yardim = Label(acilir_pencere, text= bilgilendirme)
    yardim.config(font=("Times New Roman", 15))
    yardim.grid(column=11, row=11)
    yardim.grid()

yardim_butonu= Button(acilir_pencere, text=" Yardım", command= yardim)
yardim_butonu.config(font=("Times New Roman", 15),fg="black", bg="white")
yardim_butonu.grid()

cikis = Button(acilir_pencere, text="Sonlandır.", command=quit)
cikis.config(font=("Times New Roman", 15),fg="black", bg="white")
cikis.grid()

acilir_pencere.mainloop()
