from tkinter import *
from tkinter import messagebox
# import tkinter as tk
import trjara
# import sqlara
import job4

import time


index1 = '-1'

array2 = {}

anapencere=Tk()

kisikart = {}

anapencere.title("Rehber v2.01 BETA")
anapencere.geometry("800x600+50+100")


def set_text(e,text):
    e.delete(0,END)
    e.insert(0,text)
    return

def kisikartkaydet():
    kisikart['tel1'] = tel1.get()
    kisikart['isim1'] = isim1.get()
    kisikart['aciklama1'] = aciklama1.get()
    kisikart['mail1'] = mail1.get()
    kisikart['faks1'] = faks1.get()
    kisikart['adres1'] = adres1.get()
    kisikart['tel2'] = tel2.get()
    kisikart['cep1'] = cep1.get()
    kisikart['tel3'] = tel3.get()
    kisikart['diger1'] = diger1.get()
    kisikart['ilgili1'] = ilgili1.get()
    kisikart['user'] = '-2'
    kisikart['time'] = job4.timepul()


def kisikartyukle(index):
    global kisikart,array2,index1
    index1 = array2[index]['kno']


    kisikart, lenks = trjara.idnodanara(array2[index]['kno'])
    set_text(tel1, kisikart['tel1'])
    set_text(isim1, kisikart['isim1'])
    set_text(aciklama1, kisikart['aciklama1'] )
    set_text(mail1, kisikart['mail1'])
    set_text(faks1,  kisikart['faks1'] )
    set_text(adres1,kisikart['adres1'])
    set_text(tel2, kisikart['tel2'])
    set_text(cep1, kisikart['cep1'])
    set_text(tel3,  kisikart['tel3'] )
    set_text(diger1, kisikart['diger1'])
    set_text(ilgili1, kisikart['ilgili1'])
    labelindex['text'] ='indexno: ' + index1 + ' time: ' +  kisikart['time'] + ' t. kayıt sayısı: ' + lenks + \
                        ' user: ' + kisikart['user']




def onselect(evt):

    w = evt.widget
    if len(w.curselection()) < 1:
        return

    index = int(w.curselection()[0])
    kisikartyukle(index)


lvalues3 = []
var = StringVar(value=lvalues3)

metin = Listbox(fg = "blue",font="Helvetica 13 bold", listvariable=var)
metin.configure(bg='yellow')

metin.configure(selectbackground='red')

metin.place(relx=0.0,rely=0.05,relheight=0.8,relwidth=0.4)

metin.bind('<<ListboxSelect>>', onselect)

tk_ara1 = StringVar()


def araf1():
    aranacak = ara1.get()
    global lvalues3, lvalues2, lvalues1, array2
    array2 = trjara.isimdenara(aranacak)
    lvalues3 = job4.tolist(array2)
    var = StringVar(value=lvalues3)
    metin['listvariable'] = var
    metin.select_clear(0, "end")
    metin.select_set(0)
    if (len(lvalues3) > 0):
        kisikartyukle(0)


isim1 =Entry(width=20)
isim1.place(relx=0.5,rely=0.04, relheight=0.04,relwidth=0.47)

ilgili1 =Entry(width=20)
ilgili1.place(relx=0.5,rely=0.12, relheight=0.04,relwidth=0.47)

tel1 =Entry(width=20)
tel1.place(relx=0.43,rely=0.20, relheight=0.04,relwidth=0.20)

faks1 =Entry(width=20)
faks1.place(relx=0.77,rely=0.20, relheight=0.04,relwidth=0.20)

tel2 =Entry(width=20)
tel2.place(relx=0.43,rely=0.28, relheight=0.04,relwidth=0.20)

tel3 =Entry(width=20)
tel3.place(relx=0.43,rely=0.36, relheight=0.04,relwidth=0.20)

cep1 =Entry(width=20)
cep1.place(relx=0.77,rely=0.28, relheight=0.04,relwidth=0.20)

diger1 =Entry(width=20)
diger1.place(relx=0.77,rely=0.36, relheight=0.04,relwidth=0.20)

adres1 =Entry(width=30)
adres1.place(relx=0.43,rely=0.47, relheight=0.07,relwidth=0.55)

mail1 =Entry(width=30)
mail1.place(relx=0.43,rely=0.58, relheight=0.04,relwidth=0.55)

aciklama1 =Entry(width=30)
aciklama1.place(relx=0.43,rely=0.67, relheight=0.04,relwidth=0.55)

label1=Label()
label1.config(text="isim")
label1.place(relx=0.43,rely=0.0, relheight=0.04,relwidth=0.55)

label2=Label()
label2.config(text="ilgili kişi")
label2.place(relx=0.46,rely=0.09, relheight=0.02,relwidth=0.55)

label3=Label()
label3.config(text="faks")
label3.place(relx=0.60,rely=0.175, relheight=0.02,relwidth=0.55)

label4=Label()
label4.config(text="tel")
label4.place(relx=0.45,rely=0.175, relheight=0.02,relwidth=0.15)

label5=Label()
label5.config(text="cep")
label5.place(relx=0.60,rely=0.250, relheight=0.02,relwidth=0.55)

label6 = Label()
label6.config(text="tel")
label6.place(relx=0.45,rely=0.250, relheight=0.02,relwidth=0.15)

label7=Label()
label7.config(text="diger")
label7.place(relx=0.60,rely=0.330, relheight=0.02,relwidth=0.55)


label8=Label()
label8.config(text="tel")
label8.place(relx=0.45,rely=0.330, relheight=0.02,relwidth=0.15)


label9=Label()
label9.config(text="adres")
label9.place(relx=0.49,rely=0.440, relheight=0.02,relwidth=0.45)

label10=Label()
label10.config(text="mail")
label10.place(relx=0.49,rely=0.550, relheight=0.02,relwidth=0.45)

label11=Label()
label11.config(text="aciklama")
label11.place(relx=0.49,rely=0.635, relheight=0.02,relwidth=0.45)

labelindex=Label()
labelindex.config(text="indexno:.... time:..... kayıt sayısı:..... ")
labelindex.place(relx=0.41,rely=0.79, relheight=0.02,relwidth=0.65)

ara1 =Entry(width=20,textvariable=tk_ara1, validate="all")
ara1.place(relx=0.0,rely=0.0, relheight=0.04,relwidth=0.4)
ara1.bind("<KeyRelease>", (lambda event:araf1()))


def kaydet():
    if not messagebox.askokcancel("Kaydet", "Kayıt edilsin mi?"):
        return
    kisikartkaydet()
    import isle2
    isle2.isles(index1, kisikart)
    set_text(ara1, kisikart['isim1'])
    araf1()


def yeni():
    set_text(ara1, '**yeni**')
    araf1()
    if (len(lvalues3) < 1):
        import isle2
        islem =isle2.isles('-1', {})
        set_text(ara1, '**yeni**')
        araf1()



buton=Button(anapencere)
buton.config(text="Yeni ",command=yeni)
buton.config(width=40,height=3,font=("Arial",15,"bold"),fg="#9933ff")
buton.place(relx=0.0,rely=1.0, anchor=SW)

buton2=Button(anapencere)
buton2.config(text="Kaydet",command=kaydet)
buton2.config(width=40,height=3,font=("Arial",15,"bold"),fg="#9933ff")
buton2.place(relx=1.1,rely=1.0,anchor=SE)
anapencere.resizable(0,0)
araf1()
ara1.focus()
anapencere.mainloop()
