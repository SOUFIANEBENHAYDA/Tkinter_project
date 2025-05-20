from tkinter import *
import csv
from tkinter import messagebox
from PIL import Image, ImageTk

import ptj

def Ajout_admin():
    def inscrire():
        if entry3.get()=="998877":
            admin=ptj.Admin(entry1.get(), entry2.get())
            admin.inscription()
            
            messagebox.showinfo("Success", "Le neveau admin ete ajoute")
            root.destroy()
            login()
        else:
            messagebox.showerror("Error #444", "Le code de manager est incorrect")
            entry3.delete(0, END)

    root = Tk()
    root.title("New Admin")
    root.geometry("400x500")
    root.configure(bg="#E8F0FE")
    title = Label(root, text="Neveau Admin", font=("Segoe UI", 24, "bold"), bg="#E8F0FE", fg="#3F72AF")
    title.pack(pady=30)
    frame = Frame(root, bg="#E8F0FE")
    frame.pack(pady=10)
    user = Label(frame, text="neveau utilisateur", font=("Segoe UI", 12), bg="#E8F0FE", fg="#555555")
    user.pack(anchor="w")
    entry1 = Entry(frame, width=30, font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    entry1.pack(pady=5, ipadx=5, ipady=3)
    icon = PhotoImage(file="icon4.png")
    root.iconphoto(False, icon)

    password = Label(frame, text="son mot de passe", font=("Segoe UI", 12), bg="#E8F0FE", fg="#555555")
    password.pack(anchor="w")
    entry2 = Entry(frame, show="*", width=30, font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    entry2.pack(pady=5, ipadx=5, ipady=3)
    
    manager = Label(frame, text="Code de manager :", font=("Segoe UI", 12), bg="#E8F0FE", fg="#555555")
    manager.pack(anchor="w")
    entry3 = Entry(frame, width=30,show="*", font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    entry3.pack(pady=5, ipadx=5, ipady=3)

    btn_login = Button(frame,text="Se connecter",font=("Segoe UI", 12, "bold"),bg="#4CAF50",fg="white",padx=20,pady=8,command=inscrire)
    btn_login.pack(pady=20)


def login():
    def aj_ad():
        root.destroy()
        Ajout_admin()

    root = Tk()
    root.title("Connexion")
    root.geometry("400x500")
    root.configure(bg="#E8F0FE")

    title = Label(root, text="Connexion", font=("Segoe UI", 24, "bold"), bg="#E8F0FE", fg="#3F72AF")
    title.pack(pady=30)
    
    frame = Frame(root, bg="#E8F0FE")
    frame.pack(pady=10)
    
    user = Label(frame, text="Nom d'utilisateur", font=("Segoe UI", 12), bg="#E8F0FE", fg="#555555")
    user.pack(anchor="w")
    
    entry1 = Entry(frame, width=30, font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    entry1.pack(pady=5, ipadx=5, ipady=3)
    
    password = Label(frame, text="Mot de passe", font=("Segoe UI", 12), bg="#E8F0FE", fg="#555555")
    password.pack(anchor="w")
    
    entry2 = Entry(frame, show="*", width=30, font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    entry2.pack(pady=5, ipadx=5, ipady=3)
    
    icon = PhotoImage(file="icon3.png")
    root.iconphoto(False, icon)

    def verifier():
        username = entry1.get()
        password = entry2.get()

        entry1.delete(0,END)
        entry2.delete(0,END)

        ad=ptj.Admin(username,password)
        if ad.verifier():
            root.destroy()
            ouvrir() 
        else:
            messagebox.showerror("Échec", "Identifiant incorrect !")

    btn_login = Button(frame,text="Se connecter",font=("Segoe UI", 12, "bold"),bg="#4CAF50",fg="white",padx=20,pady=8,command=verifier)
    btn_login.pack(pady=20)

    btn_login = Button(frame,text="Ajouter admin",font=("Segoe UI", 12, "bold"),bg="#4CAF50",fg="white",padx=20,pady=8,command=aj_ad)
    btn_login.pack(pady=20)
    mainloop()

def ouvrir():
    
    root = Tk()
    root.title("Gestion Pharmacy")
    root.geometry("800x600")
    root.config(bg="#E6F7FF")
    
    image = Image.open("pharmacy (2).jpg")
    image = image.resize((800, 600), Image.Resampling.LANCZOS)
    back_g = ImageTk.PhotoImage(image)
    
    background_label = Label(root, image=back_g)
    background_label.image = back_g  # Garde une référence
    background_label.place(relwidth=1, relheight=1)
    
    icon = PhotoImage(file="icon2.png")
    root.iconphoto(False, icon)
    
    def Ajouter():
        n = nom.get()
        m = molecule.get()
        d = dosage.get()
        p = prix.get()
        s = stock.get()
        e = expiration.get()
        f = fabricant.get()

        if n!="" and m!="" and d!="" and p!="" and s!="" and e!="" and f!="":
            nom.delete(0, END)
            molecule.delete(0, END)
            dosage.delete(0, END)
            prix.delete(0, END)
            stock.delete(0, END)
            fabricant.delete(0, END)
            expiration.delete(0, END)
            
            med = ptj.Medicament(n,m,d,p,s,e,f,)
            phar  = ptj.Pharmacie()
            phar.Ajouter(med)
        else:
            messagebox.showwarning("Error", "tu doit remplire tous les champs")



    def supprimer():
        n2 = nom.get()
        phar = ptj.Pharmacie()
        dose=dosage.get()

        ind=listbox.curselection()
        med=listbox.get(ind)
        print("->", med)
        medica=list(med)
        phar.Supprimer(medica[0], med[2], -1)
        affichier()

        '''
        if stock.get()=="":
        else:
            q2 = int(stock.get())
            phar.Supprimer(n2, dose, q2)
        nom.delete(0, END)
        dosage.delete(0, END)
        stock.delete(0, END)
        '''


    def effacer():
        nom.delete(0, END)
        molecule.delete(0, END)
        dosage.delete(0, END)
        prix.delete(0, END)
        stock.delete(0, END)
        fabricant.delete(0, END)
        expiration.delete(0, END)

    def affichier():
        ph=ptj.Pharmacie()
        content=ph.Affichier_tout()
        listbox.delete(0, END)


        i=0
        for cnt in content:
            listbox.insert(i, cnt)
            i+=1
    def Rechercher():
        med=supp.get()
        sible=med.split(" ")[0]
        dose=med.split(" ")[1]

        ph=ptj.Pharmacie()
        result=ph.Rechercher(sible, dose)
        if len(result)>0:
            mess="le Medicament: ["+result[0]+"] exist"
            messagebox.showinfo("Success", mess)
            listbox.delete(0, END)
            listbox.insert(0,result)
        else:
            listbox.delete(0, END)
            messagebox.showwarning("Error 404", "This medicament not Found")
            listbox.insert(0,"Not found!!")




    frm = Frame(root, bg="#E6F7FF")
    frm.pack(pady=3)
    
    Label(frm, text="Nom :", font=("Segoe UI", 10, "bold"), bg="#E6F7FF", fg="black").grid(row=0, column=0, sticky="w")
    nom = Entry(frm, width=30, bg="#E6F7FF", font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    nom.grid(row=0, column=1, padx=10, pady=5)
    
    Label(frm, text="Molécule :", font=("Segoe UI", 10, "bold"), bg="#E6F7FF", fg="black").grid(row=1, column=0, sticky="w")
    molecule = Entry(frm, width=30, bg="#E6F7FF", font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    molecule.grid(row=1, column=1, padx=10, pady=5)
    
    Label(frm, text="Dosage :", font=("Segoe UI", 10, "bold"), bg="#E6F7FF", fg="black").grid(row=2, column=0, sticky="w")
    dosage = Entry(frm, width=30, bg="#E6F7FF", font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    dosage.grid(row=2, column=1, padx=10, pady=5)
    
    Label(frm, text="Prix :", font=("Segoe UI", 10, "bold"), bg="#E6F7FF", fg="black").grid(row=3, column=0, sticky="w")
    prix = Entry(frm, width=30, bg="#E6F7FF", font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    prix.grid(row=3, column=1, padx=10, pady=5)
    
    Label(frm, text="Stock :", font=("Segoe UI", 10, "bold"), bg="#E6F7FF", fg="black").grid(row=4, column=0, sticky="w")
    stock = Entry(frm, width=30, bg="#E6F7FF", font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    stock.grid(row=4, column=1, padx=10, pady=5)
    
    Label(frm, text="Expiration :", font=("Segoe UI", 10, "bold"), bg="#E6F7FF", fg="black").grid(row=5, column=0, sticky="w")
    expiration = Entry(frm, width=30, bg="#E6F7FF", font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    expiration.grid(row=5, column=1, padx=10, pady=5)
    
    Label(frm, text="Fabricant :", font=("Segoe UI", 10, "bold"), bg="#E6F7FF", fg="black").grid(row=6, column=0, sticky="w")
    fabricant = Entry(frm, width=30, bg="#E6F7FF", font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    fabricant.grid(row=6, column=1, padx=10, pady=5)
    
    btn_frm = Frame(root, bg="#E6F7FF")
    btn_frm.pack(pady=1)
    Button(btn_frm, text="Ajouter", font=("Segoe UI", 8, "bold"), bg="#E6F7FF", fg="black", bd=1, padx=20, pady=8,command=Ajouter).grid(row=0, column=0, padx=5)


    Button(btn_frm, text="Supprimer", font=("Segoe UI", 8, "bold"), bg="#E6F7FF", fg="black", bd=1, padx=20, pady=8,command=supprimer).grid(row=0, column=1, padx=5)

    #Button(btn_frm, text="Afficher", font=("Segoe UI", 8, "bold"), bg="#E6F7FF", fg="black", bd=1, padx=20, pady=8).grid(row=0, column=2, padx=5)

    Button(btn_frm, text="Afficher Tout", font=("Segoe UI", 8, "bold"), bg="#E6F7FF", fg="black", bd=1, padx=20, pady=8, command=affichier).grid(row=0, column=5, padx=5)

    Button(btn_frm, text="Effacer", font=("Segoe UI", 8, "bold"), bg="#E6F7FF", fg="black", bd=1, padx=20, pady=8, command=effacer).grid(row=0, column=6, padx=5)
    dem = Frame(root, bg="#E6F7FF")
    dem.pack(pady=2)

    Button(dem, text="Rechercher", font=("Segoe UI", 8, "bold"),command=Rechercher, bg="#E6F7FF", fg="black", bd=1, padx=20, pady=8).grid(row=1, column=4)

    supp = Entry(dem, width=30, bg="#E6F7FF", font=("Segoe UI", 12), relief="flat", highlightbackground="#007ACC", highlightthickness=1)
    supp.grid(row=1, column=1, padx=10, pady=10)
    
    sur_frm = Frame(root, bg="#E6F7FF")
    sur_frm.pack(pady=2)
    
    listbox = Listbox(sur_frm, width=90, height=10, font=("Segoe UI", 8, "bold"), bg="#E6F7FF", fg="black", bd=1, highlightbackground="#007ACC", highlightthickness=1)
    listbox.pack(pady=10)
    
    mainloop()
    
login()

#waaaaaaaaaaa soufianeeeeeeeeee