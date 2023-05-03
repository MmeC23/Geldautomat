'''einfacher Geldautomat mit drei Funktionen'''



print("\n                 +++ GELDAUTOMAT +++\n")

#Vorgang starten
#start()   # das muss nach unten!!!!


def start():
    print("Bitte führen Sie Ihre Karte ein.")
    print("Frage an die cash mashine: Ist eine Karte eingeführt? j/n")
    karte_eingefuehrt = input(">") # WAS BEDEUTET DIESES > IN DIESEM FALLE???
    
    if karte_eingefuehrt == "j":
        print("Bitte warten Sie einen Moment.")
        import time
        time.sleep(3.0)
        auswahl_menue()
    else:
        start()
 
      
def auswahl_menue():
    print("Bitte wählen Sie aus folgenden Optionen: ")
    print("1 - Auszahlung")
    print("2 - Einzahlung")
    print("3 - Kontostand anzeigen")
    print("x - Abbruch")
    # evt. Zeit zum Auswählen ist abgelaufen
    auswahl = input(">")
    
    if auswahl == "1":
        auswahl_auszahlung()
    elif auswahl == "2":
        auswahl_einzahlung()
    elif auswahl == "3":
        auswahl_kontostand()
    elif auswahl == "x":
        auswahl_abbruch()
        start()
    else:
        auswahl_menue()
    

def auswahl_auszahlung():
    print("Bitte wählen Sie den gewünschten Betrag.")
    print("1 - 50,00 Euro")
    print("2 - 100,00 Euro")
    print("3 - 200,00 Euro")
    print("4 - 500,00 Euro")
    print("5 - gewünschten Auszahlungsbetrag selbst eingeben")
    print("x - Abbruch")    
     
    auszahlungsbetrag = input(">")
    if auszahlungsbetrag == "1":       
        print("Bitte bestätigen Sie den Auszahlungsbetrag von 50,00 Euro mit Ihrer Geheimzahl.")
        pin_eingabe()
    elif auszahlungsbetrag == "2":       
        print("Bitte bestätigen Sie den Auszahlungsbetrag von 100,00 Euro mit Ihrer Geheimzahl.")
        pin_eingabe()
    elif auszahlungsbetrag == "3":       
        print("Bitte bestätigen Sie den Auszahlungsbetrag von 200,00 Euro mit Ihrer Geheimzahl.")
        pin_eingabe()
    elif auszahlungsbetrag == "4":       
        print("Bitte bestätigen Sie den Auszahlungsbetrag von 500,00 Euro mit Ihrer Geheimzahl.")
        pin_eingabe()
    elif auszahlungsbetrag == "5":
        auszahlungsbetrag_wunsch = ">"
        auszahlungsbetrag_wunsch = float(input("Bitte geben Sie Ihren gewünschten Auszahlungsbetrag ein: >"))
        print("Ihre Auszahlung beträgt %.2f Euro." % auszahlungsbetrag_wunsch) #ALT
        #print("Ihre Auszahlung beträgt {0:.2f} Euro." .format(auszahlungsbetrag_wunsch)) #NEU
        pin_eingabe()
    elif auszahlungsbetrag == "x":       
        auswahl_abbruch()
    else:
        auswahl_auszahlung()


def pin_eingabe():
    pin = input("Bitte geben Sie Ihre Geheimzahl ein.")
    if pin == "1111":
        print("Einen Moment bitte, Ihr Vorgang wird bearbeitet.")
        import time
        time.sleep(5)
        print("Bitte entnehmen Sie Ihre Karte.")
        time.sleep(3)
        print("Bitte entnehmen Sie Ihr Geld. Auf Wiedersehen!")
        time.sleep(15)
        start()
    elif pin == "x":
        print("Der Vorgang wurde abgebrochen. Bitte entnehmen Sie Ihre Karte.")  
    elif pin != "1111": # Lösung für Pin 3x falsch finden!!!!
        print("Die eingegebene Pin ist leider falsch. Bitte geben Sie Ihre Geheimzahl erneut ein.")
        pin_eingabe()
        
    '''elif time.sleep(10.0): # das funktioniert leider nicht, noch Lösung finden!
        print("Sie haben keine Eingabe getätigt. Bitte entnehmen Sie Ihre Karte.")
        time.sleep(15)
        start()'''
        
        
def auswahl_abbruch():
    print("Der Vorgang wurde abgebrochen. Bitte entnehmen Sie Ihre Karte.")


'''def auswahl_einzahlung(): #SPÄTER
    print("    ")'''


'''def auswahl_kontostand(): #SPÄTER
    print("")'''
    
        
        
        
#Vorgang starten
start()
    

