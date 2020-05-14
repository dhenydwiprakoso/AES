from tkinter import *
root=Tk()
root.geometry("800x600")
root.title("AES-CTR with BBS")

frame=Frame(root,bg='lightblue')
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)
#-------------------definisi function untuk kriptografi-----------

#---------------definisi function untuk tampilan halaman-------
def home():
    frame=Frame(root,bg='lightblue')
    frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)
    label=Label(frame, font=('arial', 15, 'bold'), text="AES-CTR with BBS", fg="steel blue" , anchor='w')
    label.place(relx=0.31,rely=0.15)
    label=Label(frame, font=('arial', 10, 'bold'), text="Aplikasi untuk Enkripsi dan Dekripsi menggunakan AES", fg="steel blue" , anchor='w')
    label.place(relx=0.12,rely=0.25)
    label=Label(frame, font=('arial', 10, 'bold'), text="Silahkan pilih apa yang ingin Anda lakukan : ", fg="steel blue" , anchor='w')
    label.place(relx=0.19,rely=0.45)
    btnNavEnkrip = Button(padx=6, pady = 3, bd = 10, fg="black", font=('arial', 8, 'bold'), width=5, text="Enkripsi", command=pageEnkrip)
    btnNavEnkrip.place(relx=0.5, rely=0.57, anchor=CENTER)
    btnNavDekrip = Button(padx=6, pady = 3, bd = 10, fg="black", font=('arial', 8, 'bold'), width=5, text="Dekripsi", command=pageDekrip)
    btnNavDekrip.place(relx=0.5, rely=0.65, anchor=CENTER)
    label=Label(frame, font=('arial', 10, 'bold'), text="Aplikasi ini dibuat oleh :\nDheny Dwi Prakoso \n Florin Karmina Manalu", fg="steel blue" , anchor='w')
    label.place(relx=0.33,rely=0.83)

def pageEnkrip():
    plain_text_enkrip = StringVar()
    key_enkrip = StringVar()
    cipher_text_enkrip = StringVar()


    
    frame=Frame(root,bg='lightblue')
    frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)
    label=Label(frame, font=('arial', 15, 'bold'), text="Enkripsi AES", fg="steel blue" , anchor='w')
    label.place(relx=0.38,rely=0.08)


    lblPlain = Label(frame, font=('arial', 10, 'bold'), text="Plain Text", bd=10, anchor = 'w')
    lblPlain.place(relx=0.20,rely=0.25)
    txtPlain=Entry(frame, font=('arial', 10, 'bold'), textvariable=plain_text_enkrip, bd=10, insertwidth=4,
                       bg="powder blue", justify = 'center')
    txtPlain.place(relx=0.40,rely=0.25)

    lblKey = Label(frame, font=('arial', 10, 'bold'), text="Key", bd=10, anchor = 'w')
    lblKey.place(relx=0.20,rely=0.38)
    txtKey=Entry(frame, font=('arial', 10, 'bold'), textvariable=key_enkrip, bd=10, insertwidth=4,
                       bg="powder blue", justify = 'center')
    txtKey.place(relx=0.40,rely=0.38)

    btnEnkrip = Button(padx=30, pady = 3, bd = 10, fg="black", font=('arial', 8, 'bold'), width=5, text="Enkrip sekarang", command=pageEnkrip)
    btnEnkrip.place(relx=0.5, rely=0.55, anchor=CENTER)

    lblKey = Label(frame, font=('arial', 10, 'bold'), text="Cipher Text", bd=10, anchor = 'w')
    lblKey.place(relx=0.40,rely=0.68)
    txtKey=Entry(frame, font=('arial', 10, 'bold'), textvariable=key_enkrip, bd=10, insertwidth=4,
                       bg="white", justify = 'center')
    txtKey.place(relx=0.60,rely=0.68)

    btnBackHome = Button(padx=30, pady = 3, bd = 10, fg="black", font=('arial', 8, 'bold'), width=5, text="Back to Home", command=home)
    btnBackHome.place(relx=0.5, rely=0.73, anchor=CENTER)

def pageDekrip():
    plain_text_dekrip = StringVar()
    key_dekrip = StringVar()
    cipher_text_dekrip = StringVar()


    
    frame=Frame(root,bg='lightblue')
    frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)
    label=Label(frame, font=('arial', 15, 'bold'), text="Dekripsi AES", fg="steel blue" , anchor='w')
    label.place(relx=0.38,rely=0.08)


    lblPlain = Label(frame, font=('arial', 10, 'bold'), text="Cipher Text", bd=10, anchor = 'w')
    lblPlain.place(relx=0.20,rely=0.25)
    txtPlain=Entry(frame, font=('arial', 10, 'bold'), textvariable=plain_text_dekrip, bd=10, insertwidth=4,
                       bg="powder blue", justify = 'center')
    txtPlain.place(relx=0.40,rely=0.25)

    lblKey = Label(frame, font=('arial', 10, 'bold'), text="Key", bd=10, anchor = 'w')
    lblKey.place(relx=0.20,rely=0.38)
    txtKey=Entry(frame, font=('arial', 10, 'bold'), textvariable=key_dekrip, bd=10, insertwidth=4,
                       bg="powder blue", justify = 'center')
    txtKey.place(relx=0.40,rely=0.38)

    btnEnkrip = Button(padx=30, pady = 3, bd = 10, fg="black", font=('arial', 8, 'bold'), width=5, text="Dekrip sekarang", command=pageDekrip)
    btnEnkrip.place(relx=0.5, rely=0.55, anchor=CENTER)

    lblKey = Label(frame, font=('arial', 10, 'bold'), text="Plain Text", bd=10, anchor = 'w')
    lblKey.place(relx=0.42,rely=0.68)
    txtKey=Entry(frame, font=('arial', 10, 'bold'), textvariable=key_dekrip, bd=10, insertwidth=4,
                       bg="white", justify = 'center')
    txtKey.place(relx=0.60,rely=0.68)

    btnBackHome = Button(padx=30, pady = 3, bd = 10, fg="black", font=('arial', 8, 'bold'), width=5, text="Back to Home", command=home)
    btnBackHome.place(relx=0.5, rely=0.73, anchor=CENTER)
    
#--------tombol navigasi kiri atas
bt=Button(root,text='Home',command=home)
bt.grid(column=0,row=0)

bt1=Button(root,text='Eknkripsi',command=pageEnkrip)
bt1.grid(row=0,column=1)

bt2=Button(root,text='Dekripsi',command=pageDekrip)
bt2.grid(row=0,column=2)

#--------default tampilan home
label=Label(frame, font=('arial', 15, 'bold'), text="AES-CTR with BBS", fg="steel blue" , anchor='w')
label.place(relx=0.31,rely=0.15)
label=Label(frame, font=('arial', 10, 'bold'), text="Aplikasi untuk Enkripsi dan Dekripsi menggunakan AES", fg="steel blue" , anchor='w')
label.place(relx=0.12,rely=0.25)
label=Label(frame, font=('arial', 10, 'bold'), text="Silahkan pilih apa yang ingin Anda lakukan : ", fg="steel blue" , anchor='w')
label.place(relx=0.19,rely=0.45)
btnNavEnkrip = Button(padx=6, pady = 3, bd = 10, fg="black", font=('arial', 8, 'bold'), width=5, text="Enkripsi", command=pageEnkrip)
btnNavEnkrip.place(relx=0.5, rely=0.57, anchor=CENTER)
btnNavDekrip = Button(padx=6, pady = 3, bd = 10, fg="black", font=('arial', 8, 'bold'), width=5, text="Dekripsi", command=pageDekrip)
btnNavDekrip.place(relx=0.5, rely=0.65, anchor=CENTER)
label=Label(frame, font=('arial', 10, 'bold'), text="Aplikasi ini dibuat oleh :\nDheny Dwi Prakoso \n Florin Karmina Manalu", fg="steel blue" , anchor='w')
label.place(relx=0.33,rely=0.83)

root.mainloop()
