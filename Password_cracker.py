import pyfiglet
import zipfile
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
from pyfiglet import Figlet


f = pyfiglet.figlet_format("Password cracker", font="slant", width=110 ,)
print(Fore.RED + f) 





f = pyfiglet.figlet_format("Design By HackerKD", font="digital", width=110)
print(Fore.BLUE+ f)
print(Fore.RED + "Version 1.0")



def Zip_file():
    is_running = True

    while is_running:
        print(Style.BRIGHT + Fore.MAGENTA + "-----------------------------")
        print(Style.BRIGHT + Fore.YELLOW +"ZIP File Attack")
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "1.Dictionary attack")
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "2.Back")
        print(Style.BRIGHT + Fore.MAGENTA + "*****************************")
        print("")
        

        choise = input(Fore.BLUE + "Enter your choise (1-2) : ")
        print("")

        if choise == '1':
            Dictionary_attack_zipfile()
        

      

        elif choise == '2':
            is_running = False

        else:
            print(Style.BRIGHT + Fore.CYAN + "That is not a valid choise") 



def Dictionary_attack_zipfile():
    pwd_file = input(Fore.YELLOW + "Enter password list file path : ")
    zip_file = input(Fore.YELLOW + "Enter zip file path : ")

    zip_file = zipfile.ZipFile(zip_file)
    pwd_file = open(pwd_file, 'r')

    found = False

    for password in pwd_file:
        if not found:

            try:
                zip_file.extractall(pwd=password.strip().encode())
                print(Style.BRIGHT + Fore.RED + f" Password found! = {password.strip()}")
                found = True
            except:

                found = False
                pass

            else:
                break
    if found == False:
        print(Fore.BLUE + "password not found")
        
                

    


is_running = True

while is_running:
    print(Style.BRIGHT + Fore.MAGENTA + "-----------------------------")
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "1.Zip file")
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "2.Exit")
    print(Style.BRIGHT + Fore.MAGENTA + "*****************************")
    print("")

    

    choise = input(Fore.BLUE + "Enter your choice (1-2) : ")
    print("")


    if choise == '1':
        Zip_file()
    
        
    elif choise == '2':
        is_running = False
    
    else :
        print(Style.BRIGHT + Fore.CYAN + "That is not a valid choise") 

print(Fore.MAGENTA + "Thank you for using our tool! Have a nice day")
    
