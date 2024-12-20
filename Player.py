"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe Player pour le vaisseau du joueur
"""
from Torpille import Torpille

class Player:
    def __init__(self, canvas, largeur_jeu, hauteur_jeu, interface):
        """Initialisation de l'objet joueur"""
        self.canvas = canvas
        self.largeur_jeu = largeur_jeu
        self.hauteur_jeu = hauteur_jeu

        
        # Initialisation des positions du joueur
        self.x = largeur_jeu / 2
        self.y = hauteur_jeu * (3 / 4)
        
        # Création du vaisseau sous forme de triangle
        self.id = canvas.create_rectangle(
            self.x - 15, self.y - 10,  # coin supérieur gauche
            self.x + 15, self.y + 10,  # coin inférieur droit
            fill="red",
        )
        
        self.vitesse = 8  # Vitesse du joueur 
        self.direction = 0  # 0 = pas de mouvement, 1 = droite, -1 = gauche
        
        
        # Commencer la mise à jour continue du déplacement
        self.deplacement_continue()

    def deplacement(self, direction):
        """Déplacement du joueur selon la direction."""
        self.x += self.vitesse * direction

        # Limite les déplacements à l'intérieur du jeu
        if self.x < 0:
            self.x = 0
        elif self.x > self.largeur_jeu:
            self.x = self.largeur_jeu

        # Mise à jour des coordonnées du vaisseau à chaque déplacement
        self.canvas.coords(self.id, self.x - 15, self.y - 10, self.x + 15, self.y + 10)

    def deplacer_gauche(self, event):
        """Déplacer le joueur vers la gauche.
        entrée : none 
        sortie : none"""
        self.direction = -1 

    def deplacer_droite(self, event):
        """Déplacer le joueur vers la droite.
        entrée : none
        sortie : none"""
        self.direction = 1 
    
    def arreter_deplacement(self, event):
        """Arrêter le mouvement du joueur.
        entrée : none
        sortie : none"""
        self.direction = 0  

    def deplacement_continue(self):
        """Mettre à jour la position du joueur en fonction de la direction.
        entrée : none
        sortie : none"""
        if self.direction != 0:  
            self.deplacement(self.direction)
        self.canvas.after(20, self.deplacement_continue)  

    


    
