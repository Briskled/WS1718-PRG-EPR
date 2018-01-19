class Knoten:
    """Ein Knoten besitzt einen Wert "zahl" und einen namen"""
    def __init__(self, zahl, name):
        self.zahl = zahl
        self.name = name



#Es werden Knoten initialisiert
A = Knoten(4, "A")
B = Knoten(3, "B")
C = Knoten(2, "C")
D = Knoten(1, "D")
E = Knoten(150, "E")
F = Knoten(1000, "F")
G = Knoten(1001, "G")
H = Knoten(1337, "Leet")


#Unser Graph wird durch ein Dictionary dargestellt.
#Es speichert zu jedem Knoten die Knoten, die mit dem jeweiligen Knoten verbunden sind.
Graph = {}

Graph[A] = [B, C, H, F]
Graph[B] = [A, H]
Graph[C] = [A, D, E, H, F]
Graph[D] = [C, G, H]
Graph[E] = [C, F, H, G]
Graph[F] = [A, C, H, E]
Graph[G] = [E, H, D]
Graph[H] = [A, B, C, D, E, F, G]


"""
for knoten in Graph:
    tup = Graph[knoten]
    print(knoten.name)
    for child in tup:
        print(" ", child.name)"""

bereitsbesucht = set()
def tiefensuche(startknoten, ziel):
    """Die Tiefensuche sucht einen Knoten mit dem Wert "ziel" in einem Graphen
       Beginnend mit dem startknoten"""

    
    print(startknoten.name)

    #Wenn das Ziel gefunden wurde
    if startknoten.zahl == ziel:
        bereitsbesucht.clear()
        
        #Ziel zurückgeben:
        return startknoten
    else:
        #Knoten als besucht markieren
        bereitsbesucht.add(startknoten)
        
        #Nachbarknoten besuchen und von dort aus die Tiefensuche starten
        naechsteknoten = Graph[startknoten]
        for einknoten in naechsteknoten:
            if einknoten not in bereitsbesucht:
                erg = tiefensuche(einknoten, ziel)
                if erg.zahl == ziel:
                    return erg      


            









    
    
