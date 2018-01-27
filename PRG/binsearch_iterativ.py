def binsearch(liste, x):
    """Ich gehe davon aus, dass die Liste bereits sortiert ist."""
    links = 0             #Wir Starten ganz links
    rechts = len(liste)   #und ganz rechts
    
    while links <= rechts:
        mitte = links + (rechts - links)//2;  #findet den index zwischen links
                                              #und rechts. Rundet ggf ab
        if liste[mitte] == x:
            return mitte            #Wenn das Element in der Mitte das gesuchte ist
                                    #geben wir die Position (mitte) dieses Elements zurück
        if x < liste[mitte]:        #Wenn die gesuchte Zahl kleiner ist als das Element
                                    #in der Mitte muss sich x links der momentanen Mitte befinden
            rechts = mitte-1        #links bleibt wo es ist aber rechts wird links
                                    #neben mitte gesetzt
        if x > liste[mitte]:
            links = mitte+1

    return -1       #Das wird nur ausgeführt, wenn die Binärsuche x nicht gefunden hat.
                    # -1 wird häufig zum darstellen von
                    #"undefiniert", "error" oder "kein Ergebnis" verwendet
