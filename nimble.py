import random


def newBoard(n, p):
    """
    Créer un plateau de jeu de taille n ayant un nombre de pions p.
    """
    board = []
    while len(board) != n:
        board.append(0)
    for i in range(len(board)):
        if sum(board) != p:
            board[random.randint(0, len(board)-1)] += 1
    return board


def display(board):
    """
    Affiche le plateau de jeu et le nombre de piosn que comporte chaque cases du jeu.
    """
    for i in range(len(board)):
        print(board[i], end=' | ')
    print("")
    print("----"*len(board))
    for i in range(len(board)):
        print(i+1, end=' | ')


def possibleSquare(board, i):
    """
    Regarde si le pion sélectionné peut se déplacer dans une case.

    retourne True si le pion est déplaçable
    retourne False sinon
    """
    if board[i] == 0 or i <= 0:
        return False
    else:
        return True


def selectSquare(board, i):
    """
    Regarde si la case si le pion est déplaçable.

    Si on peut le déplacer, on retourne la case sur laquelle est le pion
    Sinon on re demande au joueur une case valide
    """
    if possibleSquare(board, i) == False:
        print("Sélection impossible")
        while possibleSquare(board, i) == False:
            i = int(input("Resélectionnez un nombre : "))-1
        return possibleSquare(board, i)
    else:
        return i
        

def possibleDestination(board, i, j):
    """
    Vérifie que la destination respecte les règles du jeu.
    """
    if board[i] == 0 or j > i or j == -1:
        return False
    else:
        return True

    
def selectDestination(board, i, j):
    """
    Regarde si la destination selectionnée par le joueur est valable au regarde des règles du jeux.
    Si cette destination ne l'est pas, on refait sélectionner au joueur une destination valable,
    Sinon on renvoit j.
    """
    if possibleDestination(board, i, j) == False:
        print("Déplacement impossible")
        while possibleDestination(board, i, j) == False:
            j = int(input("Entrez une case où déplacer le pion : "))
        return possibleDestination(board, i, j)
    else:
        return j


def move(board, i, j):
    """
    Déplace le pion sélectionné i sur la destination j
    """
    if possibleDestination(board, i, j) == True:
        board[i] = board[i] - 1   
        board[j] = board[j] + 1


def lose(board):
    """
    regarde si il reste des pions à déplacer sur le plateau.
    retourne False si on ne peut plus déplacer de pions 
    retourne True sinon. 
    """
    if board[0] != sum(board):
        return False
    else:
        return True


def nimble(n, p):
    """
    Boucle de jeu permettant de jouer au jeu.
    """
    player = 1
    board = newBoard(n, p)
    display(board)
    if lose(board) == False:
        while lose(board) == False:
            print("\n \n")
            print("Player", player)
            print("")

            i = int(input("Choisissez un pion à déplacer : "))-1
            selectSquare(board, i)

            j = int(input("Choisissez une case de destination pour le pion : "))-1
            selectDestination(board, i, j)

            move(board, i, j)
            display(board)
            
            if lose(board) == True:
                break
            if player == 1:
                player = 2
            else:
                player = 1
    print("")
    print("Joueur "+str(player)+" gagne.")


taillePlateau = int(input("Choisissez une taille de plateau : "))
nbrPions = int(input("Choisissez un nombre de pions"))
nimble(taillePlateau, nbrPions)
