class Knoten:
    """Ein Knoten speichert einen Wert "zahl" und einen namen.
       Zusätzlich werden in jedem Knoten die Nachbarknoten gespeichert"""
    
    def __init__(self, zahl, name, nachbarn = []):
        self.zahl = zahl
        self.name = name
        self.nachbarn = nachbarn




A = Knoten(1, "A")
B = Knoten(2, "B")
C = Knoten(3, "C")
D = Knoten(4, "D")
E = Knoten(5, "E")

#Hier werden zu jedem Knoten die Nachbarn vermerkt, indem eine Liste mit Knoten erstellt wird,
#die in Knoten.nachbarn gespeichert wird.
#Wichtig: Wir benutzen zwar mehrmals den selben Knoten, da Klassen aber Referenztypen sind
#kann von unterschiedlichen Knoten auf den selben Knoten zugegriffen werden
A.nachbarn = [B, C]
B.nachbarn = [A]
C.nachbarn = [A, D, E]
D.nachbarn = [C]
E.nachbarn = [C]




bereitsbesucht = set()
def tiefensuche(startknoten, ziel):
    """Für eine Beschreibung der Tiefensuche: Siehe "tiefensuche dictionary.py" """
    print(startknoten.name)
    
    if startknoten.zahl == ziel:
        bereitsbesucht.clear()
        return startknoten
    else:
        bereitsbesucht.add(startknoten)

        naechsteknoten = startknoten.nachbarn
        for einknoten in naechsteknoten:
            if einknoten not in bereitsbesucht:
                erg = tiefensuche(einknoten, ziel)
                if erg != None and erg.zahl == ziel:
                    return erg      


            



