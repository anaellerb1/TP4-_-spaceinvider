"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe pour définir le vaisseau du joueur
"""
LARGEUR = 600
HAUTEUR = 400

# Définition de la classe des vaisseaux ennemis niveau 2
class Alien_2:
    def __init__(self, canvas, x, y, width, height, vitesse_x):
        """Initialisation de l'object vaisseau ennemi """
        self.canvas = canvas
        self.id = canvas.create_polygon(self.x - 15, self.x + 15, self.y + 10, fill="red")
        self.vitesse_x = 2
        self.vitesse_y = -1
        self.direction = 1
        self.life = 100

    def deplacement_alien(self):
        """Initialisation des déplacement du vaisseau ennemi """
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x2 >= LARGEUR or x1 <= 0:
            self.direction *= -1
            """self.canvas.move(self.id, 0, 20)"""  # Descend lorsque atteint le bord
        self.canvas.move(self.id, self.vitesse_x * self.direction, 0)