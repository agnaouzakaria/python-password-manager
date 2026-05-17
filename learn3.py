import getpass
from openpyxl import Workbook

password_hide='2026'

def cheak_pass():
    passw=getpass.getpass("\nEntrer ton generale password : ")
    return passw==password_hide

class Account:
    def __init__(self,webs,user,pas):
        self.webs=webs
        self.user=user
        self.pas=pas
    def __str__(self):
        return f"| Platforme : {self.webs:<9} | Username : {self.user:<9} | Password : {self.pas:<8} |\n---------------------------------------------------------------------"
Plat=[]   
def ajout():
    webs=input("Platforme : ")
    user=input("Username : ")
    pas=getpass.getpass("Password : ")
    Plat.append(Account(webs,user,pas))

def afficher():
    print("")
    if cheak_pass():
        for i in Plat:
            print(i)
    else :
         for i in Plat:
            temp=i.pas
            i.pas='******'
            print(i)   
            i.pas=temp           

def afficher_seul():
    Platforme=input("Entrer le nom du platforme : ")
    print("")
    if cheak_pass():    
        for i in Plat:
            if i.webs.lower()==Platforme.lower():
                print(i)
    else :                                
        for i in Plat:
            if i.webs.lower()==Platforme.lower():

                temp=i.pas
                i.pas='******'
                print(i)
                i.pas=temp
   
def search():
    trouver=False    
    if cheak_pass():
        plat_se=input("Entrer le nom du platforme a searcher : ")
        for i in Plat:
            if i.webs.lower()==plat_se.lower():
                print(i)
                trouver=True
        if not trouver : print(f"N'est pas un account sur {plat_se} !!! ")
    else :
        plat_se=input("Entrer le nom du platforme a searcher : ")
        for i in Plat:
            if i.webs==plat_se:
                temp=i.pas
                i.pas='******'
                print(i)
                i.pas=temp
                trouver=True

        if not trouver : print(f"N'est pas un account sur {plat_se} !!! ")

def supp():
    plat_sup=input("Entrer le nom du platforme a supprimer : ")
    trouver=False
    for i in Plat:
        if i.webs.lower()==plat_sup.lower():
            Plat.remove(i)
            trouver=True
            break
    if not trouver :
            print(f"N'est pas un account a supprimer sur {plat_sup}")

def save_exel():
    wb=Workbook()
    ws=wb.active
    ws.append([" Platforme ","Username ","Password"])
    if cheak_pass():
        for i in Plat:
            ws.append([i.webs,i.user,i.pas])
    else :
            for i in Plat:
                ws.append([i.webs,i.user,'********'])
    wb.save('Acounts.xlsx')

            

def menu():
    while True:
        print("\n 1- Ajouter un account\n 2- Affichier tous les account\n 3- Affichier un seul account\n 4- Searcher un account a une platforme \n 5- Supprimer un account \n 6- Sauvgarder les account et sortie ")
        while True:
            try:
                choix=int(input("Entrer leur choix : "))
                if choix in [1,2,3,4,5,6]:
                    break
                else :
                    print("Invalide choix ")
            except:
                print("Invalide choix")
        if choix==1:
            ajout()
        elif choix==2:
            afficher()
        elif choix==3:
            afficher_seul()
        elif choix==4:
            search()
        elif choix==5:
            supp()
        elif choix==6:
            save_exel()
            exit('File sauvgarder ')
            
    
menu()


        

    
    


