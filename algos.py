import heapq
from collections import deque


# =====================================================================
#  TRIS
# =====================================================================

def tri_a_bulles(liste):
    n = len(liste)
    if n <= 1:
        return liste
    for i in range(0, n):
        for j in range(0, n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste


def tri_insertion(liste):
    n = len(liste)
    if n <= 1:
        return liste

    for i in range(1, n):
        cle = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > cle:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle
    return liste


def tri_selection(liste):
    n = len(liste)
    if n <= 1:
        return liste

    for i in range(0, n):
        indice_min = i
        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j
        liste[indice_min], liste[i] = liste[i], liste[indice_min]
    return liste


def tri_fusion(liste):
    n = len(liste)
    if n <= 1:
        return liste

    milieu = n // 2
    return fusion(tri_fusion(liste[:milieu]), tri_fusion(liste[milieu:]))


def fusion(liste1, liste2):
    resultat = []
    i, j = 0, 0
    while i < len(liste1) and j < len(liste2):
        if liste1[i] <= liste2[j]:
            resultat.append(liste1[i])
            i += 1
        else:
            resultat.append(liste2[j])
            j += 1
    resultat.extend(liste1[i:len(liste1)])
    resultat.extend(liste2[j:len(liste2)])
    return resultat


def tri_rapide(liste):
    n = len(liste)
    if n <= 1:
        return liste

    pivot = n // 2

    gauche = [x for x in liste if x < liste[pivot]]
    milieu = [x for x in liste if x == liste[pivot]]
    droite = [x for x in liste if x > liste[pivot]]
    return tri_rapide(gauche) + milieu + tri_rapide(droite)


# =====================================================================
#  RECHERCHE
# =====================================================================

def recherche_dichotomique_recursive(liste, cle, bas=0, haut=None):
    if haut is None:
        haut = len(liste)

    sous_liste = liste[bas:haut]
    n = len(sous_liste)

    if n <= 0:
        return -1

    milieu = n // 2

    if cle == sous_liste[milieu]:
        return bas + milieu

    if cle < sous_liste[milieu]:
        return recherche_dichotomique_recursive(liste, cle, bas, bas + milieu)

    else:
        return recherche_dichotomique_recursive(liste, cle, bas + milieu + 1, haut)


def recherche_dichotomique_premiere_occurrence(liste, cle):
    resultat = -1
    i, j = 0, len(liste) - 1
    while i <= j:
        milieu = (i + j) // 2
        if cle == liste[milieu]:
            resultat = milieu
            j = milieu - 1

        elif cle < liste[milieu]:
            j = milieu - 1

        elif cle > liste[milieu]:
            i = milieu + 1

    return resultat


# =====================================================================
#  TABLEAUX
# =====================================================================

def inverser_liste(liste):
    i, j = 0, len(liste) - 1
    while i < j:
        liste[i], liste[j] = liste[j], liste[i]
        i += 1
        j -= 1
    return liste


def a_un_doublon(liste):
    vus = set()
    for x in liste:
        if x in vus:
            return True
        vus.add(x)
    return False


def valeur_est_dupliquee(liste, n):
    vus = set()
    for x in liste:
        if x == n and x in vus:
            return True
        vus.add(x)
    return False


def compter_occurrences(liste, n):
    trouves = list()
    for x in liste:
        if x == n:
            trouves.append(x)
    return len(trouves)


def somme_deux_valeurs(liste, cible):
    vus = {}
    for indice, valeur in enumerate(liste):
        complement = cible - valeur
        if complement in vus:
            return (indice, vus[complement])
        vus[valeur] = indice
    return -1


def somme_deux_valeurs_triee(liste, cible):
    i, j = 0, len(liste) - 1
    while i < j:
        if liste[i] + liste[j] == cible:
            return (i, j)
        elif liste[i] + liste[j] < cible:
            i += 1
        else:
            j -= 1

    return -1


def kadane(liste):
    if len(liste) <= 0:
        return -1
    max_global = liste[0]
    max_courant = liste[0]
    for x in liste[1:]:
        max_courant = max(x, x + max_courant)
        max_global = max(max_global, max_courant)
    return max_global


def somme_max_fenetre(liste, k):
    if len(liste) < k:
        return -1

    somme_fenetre = sum(liste[:k])
    max_global = somme_fenetre

    for i in range(k, len(liste)):
        somme_fenetre += liste[i] - liste[i - k]
        max_global = max(max_global, somme_fenetre)
    return max_global


# =====================================================================
#  MATHS
# =====================================================================

def methode_newton(f, df, depart, precision=1e-12, max_iter=100):
    x = depart
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) <= precision:
            return x
        if df(x) == 0:
            raise ValueError('Division par zéro')
        x = x - fx / dfx

    return x


def fibonacci_tableau(n):
    if n <= 1:
        return n
    fibo = [-1] * (n + 1)
    fibo[0] = 0
    fibo[1] = 1

    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    return fibo[n]


def fibonacci_iteratif(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def rendu_monnaie(pieces, montant):
    dp = [float('inf')] * (montant + 1)
    dp[0] = 0

    for i in range(1, montant + 1):
        for piece in pieces:
            if i - piece >= 0:
                dp[i] = min(dp[i], dp[i - piece] + 1)
    return dp[montant] if dp[montant] != float('inf') else -1


# =====================================================================
#  PILE
# =====================================================================

def verifier_parentheses(texte):
    ouvrants_fermants = {'{', '[', ']', '}', '(', ')'}
    correspondance = {']': '[', '}': '{', ')': '('}
    pile = []

    for x in texte:
        if x not in ouvrants_fermants:
            continue
        if x not in correspondance:
            pile.append(x)
        else:
            p = pile.pop()
            if p != correspondance[x]:
                return False

    return True


# =====================================================================
#  GRAPHES
# =====================================================================

def parcours_largeur(graphe, depart):
    visites = set()
    file = deque([depart])
    resultat = []

    while file:
        noeud = file.popleft()
        if noeud not in visites:
            visites.add(noeud)
            resultat.append(noeud)

        for voisin in graphe[noeud]:
            if voisin not in visites:
                file.append(voisin)
    return resultat


def parcours_profondeur_iteratif(graphe, depart):
    visites = set()
    pile = [depart]
    resultat = []

    while pile:
        noeud = pile.pop()
        if noeud not in visites:
            visites.add(noeud)
            resultat.append(noeud)

        for voisin in reversed(graphe[noeud]):
            if voisin not in visites:
                pile.append(voisin)
    return resultat


def parcours_profondeur_recursif(graphe, depart, visites=None):
    if visites is None:
        visites = set()

    resultat = [depart]
    visites.add(depart)

    for voisin in graphe[depart]:
        if voisin not in visites:
            visites.add(voisin)
            resultat.extend(parcours_profondeur_recursif(graphe, voisin, visites))
    return resultat


def dijkstra(graphe, depart):
    distances = {x: float('inf') for x in graphe}
    distances[depart] = 0
    tas = [(depart, 0)]
    while tas:
        noeud, distance_courante = heapq.heappop(tas)
        if distance_courante > distances[noeud]:
            continue
        for voisin, poids in graphe[noeud]:
            distance = distance_courante + poids
            if distance < distances[voisin]:
                distances[voisin] = distance
                heapq.heappush(tas, (voisin, distance))

    return distances


# =====================================================================
#  LISTES CHAÎNÉES
# =====================================================================

class Noeud:
    def __init__(self, valeur, suivant) -> None:
        self.valeur = valeur
        self.suivant = suivant


def detecter_cycle(liste_chainee):
    lent = liste_chainee
    rapide = liste_chainee
    while rapide and rapide.suivant:
        lent = lent.suivant
        rapide = rapide.suivant.suivant
        if lent == rapide:
            print("true")
            return
    print("NO")
    return False


def inverser_liste_chainee(liste_chainee):
    precedent = None
    courant = liste_chainee

    while courant:
        suivant = courant.suivant
        courant.suivant = precedent
        precedent = courant
        courant = suivant
    return precedent


# =====================================================================
#  ARBRE BINAIRE DE RECHERCHE (dictionnaire : valeur -> [gauche, droite])
# =====================================================================

def rechercher_abr(arbre, racine, nb):
    x = racine
    while x:
        if x == nb:
            return x
        gauche, droite = arbre[x]
        if nb < x:
            x = gauche
        else:
            x = droite

    return -1


def inserer_abr(arbre, racine, nb):
    x = racine
    while x is not None:
        if x == nb:
            return -1
        gauche, droite = arbre[x]
        if nb < x:
            if gauche is None:
                arbre[x][0] = nb
                arbre[nb] = [None, None]
                return 0
            x = gauche
        else:
            if droite is None:
                arbre[x][1] = nb
                arbre[nb] = [None, None]
                return 0
            x = droite

    return -1


# =====================================================================
#  DÉMONSTRATIONS (une par algorithme)
# =====================================================================

GRAPHE_EXEMPLE = {
    'A': ['B', 'C'],
    'B': ['G', 'A'],
    'C': ['A', 'G', 'F'],
    'D': ['E'],
    'E': ['D', 'F'],
    'F': ['C', 'G', 'E'],
    'G': ['B', 'F', 'C'],
}

GRAPHE_PONDERE_EXEMPLE = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)],
}


def demo_tri(fonction):
    def demo():
        liste = [23, 44, 3, 1, 1, 7, 7, 7, 6]
        print(f"Liste de départ : {liste}")
        print(f"Liste triée     : {fonction(liste[:])}")
    return demo


def demo_dichotomie_recursive():
    liste = [1, 3, 5, 7, 9, 11, 13]
    print(f"Liste triée : {liste}")
    print("Recherche de 9  -> indice", recherche_dichotomique_recursive(liste, 9))
    print("Recherche de 4  -> indice", recherche_dichotomique_recursive(liste, 4), "(absent)")


def demo_dichotomie_premiere_occurrence():
    liste = [1, 2, 4, 4, 4, 4, 9, 12]
    print(f"Liste triée : {liste}")
    print("Première occurrence de 4  -> indice",
          recherche_dichotomique_premiere_occurrence(liste, 4))
    print("Première occurrence de 5  -> indice",
          recherche_dichotomique_premiere_occurrence(liste, 5), "(absent)")


def demo_inverser():
    liste = [1, 2, 3, 4, 5]
    print(f"Avant : {liste}")
    print(f"Après : {inverser_liste(liste[:])}")


def demo_doublon():
    print("[1, 2, 3, 4]    ->", a_un_doublon([1, 2, 3, 4]))
    print("[1, 2, 3, 2]    ->", a_un_doublon([1, 2, 3, 2]))


def demo_valeur_dupliquee():
    liste = [5, 3, 5, 8, 3]
    print(f"Liste : {liste}")
    print("5 est dupliqué ?", valeur_est_dupliquee(liste, 5))
    print("8 est dupliqué ?", valeur_est_dupliquee(liste, 8))


def demo_compter():
    liste = [23, 44, 3, 1, 1, 7, 7, 7, 6]
    print(f"Liste : {liste}")
    print("Nombre de 7 :", compter_occurrences(liste, 7))
    print("Nombre de 2 :", compter_occurrences(liste, 2))


def demo_somme_deux_valeurs():
    liste = [2, 7, 11, 15]
    print(f"Liste : {liste}, cible = 9")
    print("Indices :", somme_deux_valeurs(liste, 9))
    print("Cible 100 ->", somme_deux_valeurs(liste, 100), "(impossible)")


def demo_somme_deux_valeurs_triee():
    liste = [1, 3, 4, 6, 8, 11]
    print(f"Liste triée : {liste}, cible = 14")
    print("Indices :", somme_deux_valeurs_triee(liste, 14))
    print("Cible 100 ->", somme_deux_valeurs_triee(liste, 100), "(impossible)")


def demo_kadane():
    liste = [1, -1, 7, 5, -1, 2]
    print(f"Liste : {liste}")
    print("Somme maximale d'un sous-tableau contigu :", kadane(liste))


def demo_fenetre():
    liste = [5, 0, 1, 4, 5, 2]
    print(f"Liste : {liste}, k = 3")
    print("Somme maximale sur 3 éléments consécutifs :", somme_max_fenetre(liste, 3))


def demo_newton():
    f = lambda x: x ** 2 - 5
    df = lambda x: 2 * x
    print("On cherche la racine de f(x) = x² - 5, départ x0 = 3")
    print(f"Résultat : {methode_newton(f, df, 3):.6f}  (√5 ≈ 2.236068)")


def demo_fibonacci(fonction):
    def demo():
        n = 10
        print(f"fibonacci({n}) = {fonction(n)}")
        print(f"fibonacci(30) = {fonction(30)}")
    return demo


def demo_rendu_monnaie():
    pieces = [1, 5, 6, 3]
    print(f"Pièces : {pieces}, montant = 13")
    print("Nombre minimal de pièces :", rendu_monnaie(pieces, 13))
    print("Montant 2 avec [5] ->", rendu_monnaie([5], 2), "(impossible)")


def demo_parentheses():
    for texte in ["{{{[4]}3}}", "{[(])}", "(a + b) * [c]"]:
        print(f"{texte!r:20} -> {verifier_parentheses(texte)}")


def demo_bfs():
    print(f"Graphe : {GRAPHE_EXEMPLE}")
    print("Parcours en largeur depuis 'A' :", parcours_largeur(GRAPHE_EXEMPLE, 'A'))


def demo_dfs_iteratif():
    print(f"Graphe : {GRAPHE_EXEMPLE}")
    print("Parcours en profondeur depuis 'A' :",
          parcours_profondeur_iteratif(GRAPHE_EXEMPLE, 'A'))


def demo_dfs_recursif():
    print(f"Graphe : {GRAPHE_EXEMPLE}")
    print("Parcours en profondeur depuis 'A' :",
          parcours_profondeur_recursif(GRAPHE_EXEMPLE, 'A'))


def demo_dijkstra():
    print(f"Graphe pondéré : {GRAPHE_PONDERE_EXEMPLE}")
    print("Plus courtes distances depuis 'A' :",
          dijkstra(GRAPHE_PONDERE_EXEMPLE, 'A'))


def demo_cycle():
    queue = Noeud(3, None)
    milieu = Noeud(2, queue)
    tete = Noeud(1, milieu)
    print("Liste 1 -> 2 -> 3 (sans cycle) : ", end="")
    detecter_cycle(tete)
    queue.suivant = tete
    print("Liste 1 -> 2 -> 3 -> 1 (cycle) : ", end="")
    detecter_cycle(tete)


def demo_inverser_chainee():
    queue = Noeud(3, None)
    milieu = Noeud(2, queue)
    tete = Noeud(1, milieu)
    print("Avant : 1 -> 2 -> 3")
    tete = inverser_liste_chainee(tete)
    valeurs = []
    courant = tete
    while courant:
        valeurs.append(str(courant.valeur))
        courant = courant.suivant
    print("Après :", " -> ".join(valeurs))


def demo_rechercher_abr():
    arbre = {
        50: [30, 70],
        30: [20, 40],
        70: [60, None],
        20: [None, None],
        40: [None, None],
        60: [None, None],
    }
    print(f"Arbre (valeur: [gauche, droite]) : {arbre}")
    print("Recherche de 60 ->", rechercher_abr(arbre, 50, 60))
    print("Recherche de 99 ->", rechercher_abr(arbre, 50, 99), "(absent)")


def demo_inserer_abr():
    arbre = {40: [None, None]}
    print(f"Arbre de départ : {arbre}")
    for valeur in [5, 10, 60, 0, 10]:
        code = inserer_abr(arbre, 40, valeur)
        etat = "inséré" if code == 0 else "déjà présent"
        print(f"Insertion de {valeur:>2} -> {code}  ({etat})")
    print(f"Arbre final : {arbre}")


# =====================================================================
#  CATALOGUE : (nom, catégorie, complexité temps, complexité espace, description, démo)
# =====================================================================

ALGOS = [
    ("Tri à bulles", "Tris", "O(n²)", "O(1)",
     "Échange les voisins mal ordonnés, passage après passage.",
     demo_tri(tri_a_bulles)),
    ("Tri par insertion", "Tris", "O(n²) pire cas, O(n) meilleur cas", "O(1)",
     "Insère chaque élément à sa place dans la partie déjà triée.",
     demo_tri(tri_insertion)),
    ("Tri par sélection", "Tris", "O(n²)", "O(1)",
     "Cherche le minimum et le place au début à chaque étape.",
     demo_tri(tri_selection)),
    ("Tri fusion", "Tris", "O(n log n)", "O(n)",
     "Divise en deux, trie chaque moitié, puis fusionne.",
     demo_tri(tri_fusion)),
    ("Tri rapide", "Tris", "O(n log n) en moyenne, O(n²) pire cas", "O(n) dans cette version",
     "Choisit un pivot et sépare en plus petits / égaux / plus grands.",
     demo_tri(tri_rapide)),

    ("Recherche dichotomique (récursive)", "Recherche", "O(n) ici à cause du slicing (O(log n) en théorie)", "O(n) ici (copies de sous-listes)",
     "Cherche dans une liste triée en coupant en deux, avec des sous-listes.",
     demo_dichotomie_recursive),
    ("Recherche dichotomique (1re occurrence)", "Recherche", "O(log n)", "O(1)",
     "Version itérative qui renvoie l'indice de la première occurrence.",
     demo_dichotomie_premiere_occurrence),

    ("Inverser une liste", "Tableaux", "O(n)", "O(1)",
     "Échange le premier et le dernier élément, en se rapprochant du centre.",
     demo_inverser),
    ("Détecter un doublon", "Tableaux", "O(n)", "O(n)",
     "Utilise un ensemble pour repérer une valeur déjà vue.",
     demo_doublon),
    ("Une valeur précise est-elle dupliquée ?", "Tableaux", "O(n)", "O(n)",
     "Comme ci-dessus mais seulement pour la valeur n.",
     demo_valeur_dupliquee),
    ("Compter les occurrences", "Tableaux", "O(n)", "O(k), k = nb d'occurrences",
     "Compte combien de fois une valeur apparaît.",
     demo_compter),
    ("Somme de deux valeurs (dictionnaire)", "Tableaux", "O(n)", "O(n)",
     "Trouve deux indices dont les valeurs font la cible (Two Sum).",
     demo_somme_deux_valeurs),
    ("Somme de deux valeurs (liste triée)", "Tableaux", "O(n)", "O(1)",
     "Deux pointeurs aux extrémités d'une liste triée.",
     demo_somme_deux_valeurs_triee),
    ("Kadane (sous-tableau de somme max)", "Tableaux", "O(n)", "O(1)",
     "Somme maximale d'un sous-tableau contigu.",
     demo_kadane),
    ("Fenêtre glissante (somme max sur k éléments)", "Tableaux", "O(n)", "O(1)",
     "Fait glisser une fenêtre de taille k en mettant la somme à jour.",
     demo_fenetre),

    ("Méthode de Newton", "Maths", "O(max_iter), convergence quadratique", "O(1)",
     "Approche une racine de f avec x - f(x)/f'(x).",
     demo_newton),
    ("Fibonacci (tableau)", "Maths", "O(n)", "O(n)",
     "Programmation dynamique avec un tableau.",
     demo_fibonacci(fibonacci_tableau)),
    ("Fibonacci (itératif)", "Maths", "O(n)", "O(1)",
     "Garde seulement les deux dernières valeurs.",
     demo_fibonacci(fibonacci_iteratif)),
    ("Fibonacci (récursif mémoïsé)", "Maths", "O(n)", "O(n)",
     "Récursion avec dictionnaire pour ne pas recalculer.",
     demo_fibonacci(fibonacci_memo)),
    ("Rendu de monnaie", "Maths", "O(montant × nb_pièces)", "O(montant)",
     "Nombre minimal de pièces pour atteindre un montant (programmation dynamique).",
     demo_rendu_monnaie),

    ("Vérifier les parenthèses", "Pile", "O(n)", "O(n)",
     "Vérifie que { [ ( sont bien refermés dans le bon ordre avec une pile.",
     demo_parentheses),

    ("Parcours en largeur (BFS)", "Graphes", "O(V + E)", "O(V)",
     "Explore le graphe niveau par niveau avec une file.",
     demo_bfs),
    ("Parcours en profondeur (DFS itératif)", "Graphes", "O(V + E)", "O(V)",
     "Explore en allant le plus loin possible, avec une pile.",
     demo_dfs_iteratif),
    ("Parcours en profondeur (DFS récursif)", "Graphes", "O(V + E)", "O(V)",
     "Même idée, avec la récursion.",
     demo_dfs_recursif),
    ("Dijkstra", "Graphes", "O((V + E) log V) en théorie", "O(V)",
     "Plus courtes distances depuis un sommet (poids positifs).",
     demo_dijkstra),

    ("Détecter un cycle (lièvre et tortue)", "Listes chaînées", "O(n)", "O(1)",
     "Deux pointeurs, un lent et un rapide : s'ils se croisent, il y a un cycle.",
     demo_cycle),
    ("Inverser une liste chaînée", "Listes chaînées", "O(n)", "O(1)",
     "Retourne les pointeurs 'suivant' un par un.",
     demo_inverser_chainee),

    ("Recherche dans un ABR", "Arbre binaire de recherche", "O(log n) équilibré, O(n) pire cas", "O(1)",
     "Descend à gauche ou à droite selon la valeur cherchée.",
     demo_rechercher_abr),
    ("Insertion dans un ABR", "Arbre binaire de recherche", "O(log n) équilibré, O(n) pire cas", "O(1)",
     "Descend jusqu'à la bonne place libre puis insère.",
     demo_inserer_abr),
]


# =====================================================================
#  MENU
# =====================================================================

def afficher_menu():
    print("\n" + "=" * 60)
    print("  Voici les algorithmes disponibles :")
    print("=" * 60)
    categorie_courante = None
    for numero, (nom, categorie, *_reste) in enumerate(ALGOS, start=1):
        if categorie != categorie_courante:
            print(f"\n  --- {categorie} ---")
            categorie_courante = categorie
        print(f"  {numero:>2}. {nom}")
    print("\n   0. Quitter")


def lancer_algo(numero):
    nom, categorie, temps, espace, description, demo = ALGOS[numero - 1]
    print("\n" + "-" * 60)
    print(f"  {nom}  [{categorie}]")
    print("-" * 60)
    print(f"Principe : {description}\n")
    print("Exemple :")
    demo()
    print("\nComplexité :")
    print(f"  - Temps  : {temps}")
    print(f"  - Espace : {espace}")


def main():
    while True:
        afficher_menu()
        choix = input("\nLequel veux-tu tester ? (numéro) : ").strip()

        if choix == "0":
            print("À bientôt !")
            break

        if not choix.isdigit() or not 1 <= int(choix) <= len(ALGOS):
            print("Choix invalide, entre un numéro de la liste.")
            continue

        lancer_algo(int(choix))
        input("\nAppuie sur Entrée pour revenir au menu...")


if __name__ == "__main__":
    main()