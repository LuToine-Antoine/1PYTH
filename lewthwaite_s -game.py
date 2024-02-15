import copy


def newBoard(n):
    """
    Fonction qui créé le plateau de jeu avec n repésentant la taille du plateau que l'on veut.
    la taille du plateau se définit selon la formule 4*n+1
    """
    board = []
    _ = 1

    while n <= 0:
        n = int(input("Re-définissez une taille de plateau : "))
        
    taille = 4*n+1
    
    for truc in range(taille):
        ligne = []
        board.append(ligne)
        for i in range(taille):
            ligne.append(0)
        
        if _ % 2 != 0:
            for i in range(taille):
                if i % 2 != 0:
                    ligne[i] = 1
    
                elif i % 2 == 0:
                    ligne[i] = 2

        elif _ % 2 == 0:
            for i in range(taille):
                if i % 2 != 0:
                    ligne[i] = 2
    
                elif i % 2 == 0:
                    ligne[i] = 1

        _ += 1
        
    center = int((taille-1)/2)
    board[center][center] = 0
    
    return board
    

def displayBoard(board, n):
    """
    Affiche le plateau avec des pions O pour le joueur 1, X pour le joueur 2, et . pour une case vide.
    """
    taille = 4*n+1
    boarddisp = copy.deepcopy(board)
    for i in range(len(boarddisp)):
        for j in range(len(boarddisp[i])):
            if boarddisp[i][j] == 1:
                boarddisp[i][j] = "x"
            elif board[i][j] == 2:
                boarddisp[i][j] = "o"
            elif board[i][j] == 0:
                boarddisp[i][j] = "."

    for ligne in range(len(boarddisp)):
        print(ligne+1, ' |  ', end='')
        print(*boarddisp[ligne], sep=" | ")

    print("__ __"*taille)
    print()

    for ligne in range(len(boarddisp)):  
        print("", ligne+1, sep=' ', end='')
        print("   ", end='')

    return boarddisp


def possiblePawn(board, player, i, j):
    """
    Regarde si l'on peut sélectionner le pion au regard des règles du jeu
    """
    # Gauche
    if (board[i][j] == player) and (board[i][j-1] == player):
        return True
    
    # Droite
    if (board[i][j] == player) and (board[i][j+1] == player):
        return True
    
    # Haut
    if (board[i][j] == player) and (board[i-1][j] == player):
        return True
    
    # Bas
    if (board[i][j] == player) and (board[i+1][j] == player):
        return True
    
    # Case différente de 0
    if not (board[i][j] == 0):
        return True
    return False
    

def selectPawn(board, player):
    """
    Demande au joueur de sélectionner un pion de coordonnées j,i
    Si ces coordonnées ne sont pas valides, on demande au joueur d'entrer de nouvelles valides.
    """

    i = int(input("Choisissez une coordonnée d'odronnée : "))-1
    j = int(input("Choisissez une coordonnée d'abscisse : "))-1

    if possiblePawn(board, player, i, j) == True:
        return i, j
    
    while possiblePawn(board, player, i, j) == False:
        i = int(input("Re choisissez une ordonnée :"))-1
        j = int(input("Re choisissez une abscisse :"))-1

    return i, j


def updateBoard(board, i, j, n):
    """
    Déplace le pion sélectionné à la destination choisie et affiche le tableau avec ce changement
    """
    for indexbor in range(len(board)):
        for indexlign in range(len(board)):
            if board[indexbor][indexlign] == 0:
                cozero1, cozero2 = indexbor, indexlign

    _ = board[i][j]
    board[cozero1][cozero2] = _
    board[i][j] = 0
    return displayBoard(board, n)


def rechercheZero(board):
    """
    Fonction qui trouve le zéro dans le plateau et renvoit ses coordonnées
    """
    coordonnees = []
    while coordonnees == []:
        for indexLigneZero in range(len(board)):
            for indexColonneZero in range(len(board)):
                if board[indexLigneZero][indexColonneZero] == 0:
                    coordonneesLigneZero = indexLigneZero+1
                    coordonneesColonneZero = indexColonneZero+1
                    coordonnees.append(coordonneesLigneZero)
                    coordonnees.append(coordonneesColonneZero)
                    return coordonnees


def again(board, player, coordonneesLigneZero, coordonneesColonneZero):
    """
    regarde si un des deux joueurs ne peut plus déplacer de pions.
    Si les deux joueurs peuvent encore déplacer un pion, la partie continue,
    Si les deux joueurs ne peuvent plus en déplacer, le jeu s'arrête
    """
    taille = len(board)-1

    if coordonneesLigneZero != 0:
        if board[coordonneesLigneZero-1][coordonneesColonneZero-2] == player:
            return True
                
    if coordonneesColonneZero != 0:
        if board[coordonneesLigneZero-2][coordonneesColonneZero-1] == player:
            return True
                    
    if coordonneesLigneZero != taille:
        if board[coordonneesLigneZero][coordonneesColonneZero-1] == player:
            return True
                    
    if coordonneesColonneZero != taille:
        if board[coordonneesLigneZero-1][coordonneesColonneZero+1] == player:
            return True   
    
    return False


def lewthwaite(n):
    """
    Boucle de jeu, permet de jouer au jeu.
    """
    player = 1
    board = newBoard(n)
    displayBoard(board, n)
    print("")
    coordonnees = rechercheZero(board)
    coordonneesLigneZero = coordonnees[0]
    coordonneesColonneZero = coordonnees[1]
   
    while again(board, player, coordonneesLigneZero, coordonneesColonneZero):
        print("")
        print("Player", player)
        print("")

        i, j = selectPawn(board, player)
        updateBoard(board, i, j, n)
        coordonnees = rechercheZero(board)
        coordonneesLigneZero = coordonnees[0]
        coordonneesColonneZero = coordonnees[1]
        if again(board, player, coordonneesLigneZero, coordonneesColonneZero) == False:
            break
        if player == 1:
            player = 2
        else:
            player = 1

    if player == 1:
        print("")
        print("Joueur 2 gagne.")
    
    else:
        print("")
        print("Joueur 1 gagne.")


lewthwaite(1)
