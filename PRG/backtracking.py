def coin_amount(geldbetrag):
    """Der Geldbetrag muss in cent angegeben werden."""
    print("Restgeld", geldbetrag)
    if geldbetrag >= 11:                            #Wenn wir noch mehr als 11 Cent im Betrag haben
        return 1 + coin_amount(geldbetrag - 11)     #Geben wir eine Münze zurück. Und zusätzlich
                                                    #die Anzahl der Münzen, die derselbe Algorithmus
                                                    #mit dem Geldbetrag abzüglich der 11-Cent-Münze
                                                    #liefert
    if geldbetrag >= 5:
        return 1 + coin_amount(geldbetrag - 5)
    if geldbetrag >= 1:
        return 1 + coin_amount(geldbetrag - 1)
    else:                                           #Wenn kein Geld mehr übrig ist
        return 0                                    #geben wir auch kein Geld mehr zurück


