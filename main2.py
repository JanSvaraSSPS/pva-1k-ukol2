import sys

while True:
    print("------------------------------")
    print("Vítejte v kámen, nůžky, papír!")
    print("------------------------------")
    print("Možnosti:")
    print("     - Vybrat režim (v)")
    print("     - Odejít (o)")
    
    while True:
        akce = input("Akce: ")
        if akce == "v":
            while True:
                print(f"\n------------------------------")
                print("Režimy")
                print("------------------------------")
                print("Možnosti:")
                print("     - Normální hra (n)")
                print("     - Zpět (z)")
                
                akce_rezim = input("Akce: ")
                if akce_rezim == "n":
                    print("Zde bude hra...")
                    sys.exit()
                elif akce_rezim == "z":
                    break
                else:
                    print("Neznámá akce!\n")
            break 
            
        elif akce == "o":
            print("Ukončuji program...")
            sys.exit()
            
        else:
            print("Neznámá akce!\n")
            break
