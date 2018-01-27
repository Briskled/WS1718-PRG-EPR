def binsearch(liste, x, links, rechts):
    if rechts < links:      #wenn rechts kleiner als links ist
        return -1           #haben wir x nicht gefunden

    mitte = links + (rechts - links)//2
    if x == liste[mitte]:   #Wenn das mittlere Element x ist haben wir x gefunden
        return mitte        #und geben die Position zurück

    if x < liste[mitte]:                            #Wenn x links neben der Mitte liegt
        return binsearch(liste, x, links, mitte-1)  #Führen wir die binäre Suche nur noch
                                                    #auf den Elementen links von mitte aus
    if x > liste[mitte]:
        return binsearch(liste, x, mitte+1, rechts)
    
