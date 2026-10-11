import random

while True:
    print("------------------------------")
    print("Vítejte v kámen, nůžky, papír!")
    print("------------------------------")
    print("Možnosti:")
    print("     - Vybrat režim (v)")
    print("     - Odejít (o)")
    
    akce = input("Akce: ")

    if akce == "v":
        while True:
            print("\n------------------------------")
            print("Režimy")
            print("------------------------------")
            print("Možnosti:")
            print("     - Normální hra (n)")
            print("     - Nejlepší z pěti (p)")
            print("     - Nemožný režim (x)")
            print("     - Zpět (z)")
            
            akce_rezim = input("Akce: ")
            
            if akce_rezim == "n":
                vyhry = 0
                prohry = 0
                remizy = 0
                
                while True:
                    while True:
                        volba_hrac = input("Vaše volba (k/n/p, nebo q pro konec): ")
                        if volba_hrac == "k" or volba_hrac == "n" or volba_hrac == "p" or volba_hrac == "q":
                            break
                        else:
                            print("Neznámá volba!\n")
                    
                    if volba_hrac == "q":
                        print("\n------------------------------")
                        print("Konečné skóre:")
                        print("Výhry:", vyhry)
                        print("Prohry:", prohry)
                        print("Remízy:", remizy)
                        print("------------------------------\n")
                        break
                    
                    volba_pc = random.choice(["k", "n", "p"])
                    print("Počítač zvolil:", volba_pc)
                    
                    if volba_hrac == volba_pc:
                        print("Remíza!\n")
                        remizy = remizy + 1
                    elif volba_hrac == "k" and volba_pc == "n":
                        print("Vyhráli jste kolo!\n")
                        vyhry = vyhry + 1
                    elif volba_hrac == "n" and volba_pc == "p":
                        print("Vyhráli jste kolo!\n")
                        vyhry = vyhry + 1
                    elif volba_hrac == "p" and volba_pc == "k":
                        print("Vyhráli jste kolo!\n")
                        vyhry = vyhry + 1
                    else:
                        print("Prohráli jste kolo!\n")
                        prohry = prohry + 1
                    
                    print("Aktuální stav -> Výhry:", vyhry, "| Prohry:", prohry, "| Remízy:", remizy, "\n")

            elif akce_rezim == "p":
                vyhry = 0
                prohry = 0
                remizy = 0
                kolo = 1
                
                while kolo <= 5:
                    print("--- Kolo", kolo, "z 5 ---")
                    
                    while True:
                        volba_hrac = input("Vaše volba (k/n/p): ")
                        if volba_hrac == "k" or volba_hrac == "n" or volba_hrac == "p":
                            break
                        else:
                            print("Neznámá volba!\n")
                    
                    volba_pc = random.choice(["k", "n", "p"])
                    print("Počítač zvolil:", volba_pc)
                    
                    if volba_hrac == volba_pc:
                        print("Remíza!\n")
                        remizy = remizy + 1
                    elif volba_hrac == "k" and volba_pc == "n":
                        print("Vyhráli jste kolo!\n")
                        vyhry = vyhry + 1
                    elif volba_hrac == "n" and volba_pc == "p":
                        print("Vyhráli jste kolo!\n")
                        vyhry = vyhry + 1
                    elif volba_hrac == "p" and volba_pc == "k":
                        print("Vyhráli jste kolo!\n")
                        vyhry = vyhry + 1
                    else:
                        print("Prohráli jste kolo!\n")
                        prohry = prohry + 1
                    
                    kolo = kolo + 1
                
                print("------------------------------")
                print("Konečné skóre po 5 kolech:")
                print("Výhry:", vyhry)
                print("Prohry:", prohry)
                print("Remízy:", remizy)
                print("------------------------------")
                
                if vyhry > prohry:
                    print("Celkově jste vyhráli sérii!\n")
                elif prohry > vyhry:
                    print("Počítač celkově vyhrál sérii!\n")
                else:
                    print("Série skončila celkovou remízou!\n")

            elif akce_rezim == "x":
                while True:
                    while True:
                        volba_hrac = input("Vaše volba (k/n/p, nebo q pro konec): ")
                        if volba_hrac == "k" or volba_hrac == "n" or volba_hrac == "p" or volba_hrac == "q":
                            break
                        else:
                            print("Neznámá volba!\n")
                    
                    if volba_hrac == "q":
                        print()
                        break
                    
                    if volba_hrac == "k":
                        volba_pc = "p"
                    elif volba_hrac == "n":
                        volba_pc = "k"
                    elif volba_hrac == "p":
                        volba_pc = "n"
                    
                    print("Počítač zvolil:", volba_pc)
                    print("Prohráli jste!\n")

            elif akce_rezim == "z":
                print()
                break
                
            else:
                print("Neznámá akce!\n")

    elif akce == "o":
        print("Ukončuji program...")
        break

    else:
        print("Neznámá akce!\n")
