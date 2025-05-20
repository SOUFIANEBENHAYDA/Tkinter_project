from os import path, remove
import csv
from tkinter import messagebox
import sqlite3

class Medicament:
    def __init__(self, nom, molecule, dosage, prix, stock, expiration, fabricant):
        self.__nom=nom
        self.__molecule=molecule
        self.__dosage=dosage
        self.__prix=prix
        self.__stock=int(stock)
        self.__expiration=expiration
        self.__fabricant=fabricant

    #getters
    def get_nom(self):
        return self.__nom
    def get_molecule(self):
        return self.__molecule
    def get_dosage(self):
        return self.__dosage    
    def get_prix(self):
        return self.__prix
    def get_stock(self):
        return self.__stock
    def get_expiration(self):
        return self.__expiration
    def get_fabricant(self):
        return self.__fabricant
    
    #set_setters
    def set_nom(self, new):
        self.__nom=new
    def set_molecule(self, new):
        self.__molecule=new
    def set_dosage(self, new):
        self.__dosage=new
    def set_prix(self, new):
        self.__prix=new
    def set_stock(self, new):
        self.__stock=new
    def set_expiration(self, new):
        self.__expiration=new
    def set_fabricant(self, new):
        self.__fabricant=new


class Pharmacie:

    def Ajouter(self, new_med):
        if path.exists("Medicament_stock.csv")==False:
            f=open("Medicament_stock.csv", "w", newline="")
            f.close()

        if isinstance(new_med, Medicament):
        
            #Enregistrement en csv
            f=open("Medicament_stock.csv", "r")
            stock=list(csv.reader(f, delimiter=";"))
            f.close()
            for i in range(len(stock)):
                stock[i][4]=int(stock[i][4])

            pack=[new_med.get_nom(), new_med.get_molecule(),new_med.get_dosage(), new_med.get_prix(), new_med.get_stock(), new_med.get_expiration(), new_med.get_fabricant()]
            
            confirm=False
            for i in range(len(stock)):
                #comparer le nom de medicament et son dosage
                if pack[0] == stock[i][0] and pack[2]==stock[i][2]:
                    print("start if___________")
                    print("----------",i)
                    stock[i][4]+=pack[4]
                    
                    f=open("Medicament_stock.csv", "w", newline="")
                    write=csv.writer(f, delimiter=";")
                    write.writerows(stock)
                    f.close()
                    messagebox.showinfo("Success", "Le medicament ete ajoute au stock")
                    confirm=True
                    break

            if confirm==False:
                
                print("othereee-----------")
                
                f=open("Medicament_stock.csv", "a", newline="")
                write=csv.writer(f, delimiter=";")
                write.writerow(pack)
                f.close()
                messagebox.showinfo("Success", "Le medicament ete ajoute")
            
        else:
            print(f"error :<object: {new_med}> is not instance of medicament class")
        
    def Affichier_tout(self):
            #affichage en csv

            f=open("Medicament_stock.csv", "r")
            stock=list(csv.reader(f, delimiter=";"))
            f.close()

            #list of listes
            return stock

    def Supprimer(self, prod, dose, quantite=1):
            
            #supprimer prod specifier
        f = open("Medicament_stock.csv", "r")
        stock = list(csv.reader(f, delimiter=";"))
        f.close()

        for i in range(len(stock)):
            stock[i][4] = int(stock[i][4])

        for i in range(len(stock)):
            check=False
            if stock[i][0] == prod and stock[i][2]==dose:

                if quantite >= stock[i][4] or quantite <0:
                    stock.pop(i)
                    messagebox.showinfo("info", "le produit eté totalement supprimé")
                    check=True
                else:
                    messagebox.showinfo("info", "le stock eté reduite")
                    stock[i][4] -= quantite
                    check=True
                break
        if check==False:
            messagebox.askretrycancel("ERROr", "Le produit n'exist pas dans le stock !!!!")

        f = open("Medicament_stock.csv", "w", newline="")
        write = csv.writer(f, delimiter=";")
        write.writerows(stock)
        f.close()

    #vider le stock
    def Effacer(self):
        remove("Medicament_stock.csv")
        f=open("medicament_stock.csv", "w", newline="")
        f.close()


    def Rechercher(self, prod, dose):
        f=open("Medicament_stock.csv", "r")
        stock=list(csv.reader(f, delimiter=";"))
        f.close()

        for st in stock:
            if prod == st[0] and dose==st[2]:
                print("yes there is")
                return st
        return []
            
class Admin:
    def __init__(self, name, password):
        self.__name=name
        self.__pwd=password

    def verifier(self):
        f=open("users.csv", "r")
        users=list(csv.reader(f, delimiter=";"))
        f.close()
        
        for user in users:
            #print("--------->",user)
            if user[0]==self.__name and user[1]==self.__pwd:
                return True
        return False
        
    def inscription(self):
        f=open("users.csv", "a", newline="")
        insc=csv.writer(f, delimiter=";")
        insc.writerow([self.__name, self.__pwd])
        f.close()

'''
med =Medicament("doliprane", "paracitamole", "500g",20,33,2026,"med_us")
med2 =Medicament("doliprane2", "paracita", "1000g",30,12,2027,"med_us")

ph=Pharmacie()

ph.Ajouter(med)
ph.Ajouter(med2)

ph.Ajouter("test_fake_med")


print("_______________stock kaml____________________")
print(ph.Affichier_tout())

ph.Supprimer("doliprane", quantite=5)

ph.Rechercher("doliprane")
ph.Effacer()
user=Admin("soufiane", "123")
user2=Admin("youssef", "456")
user.inscription()
user2.inscription()
'''
'''
print(user.verifier())
print(user2.verifier())
'''