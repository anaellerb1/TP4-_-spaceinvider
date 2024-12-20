"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe Alien
Amélioration : créer différent type d'alien avec des spécificités 
différentes(avec peut être différente classe)
"""


class Alien:
    def __init__(self, canvas, x, y, largeur_jeu):
        """
        Initialisation d'un alien.
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15, fill="yellow")  
        self.vitesse_x = 3
        self.vitesse_y = -1
        self.direction = 1  # 1 : se déplacer vers la droite (gauche=-1) 
        self.niveau = 1
        self.largeur_jeu = largeur_jeu 

    def deplacer_aliens(self, aliens):
        """
        Méthode pour déplacer tous les aliens à chaque intervalle. 
        Si un alien touche un bord, il change de direction et descend.
        Args:
            aliens (list): Liste des aliens à déplacer

        Returns:
            None
        """
        aliens_bords = self.get_bord(aliens)
        
        if aliens_bords['Gauche'] or aliens_bords['Droite']:
            for alien in aliens:
                alien.direction *= -1 
                alien.y += 20
                alien.canvas.move(alien.id, 0, 20)
        for alien in aliens:
            alien.canvas.move(alien.id, alien.vitesse_x * alien.direction, 0)

    def get_bord(self, aliens):
        """Retourne si un alien aux extrémités (gauche/droite) touche un bord.
        Args:
            liste d'objet (aliens)
        Returns:
            Un dictionnaire (bords) avec les clés 'Gauche' et 'Droite'
        """
        bords = {'Gauche': False, 'Droite': False}
        x1, y1, x2, y2 = self.canvas.coords(aliens[0].id)
        if x1 <= 0:  
            bords['Gauche'] = True
        
        x1, y1, x2, y2 = self.canvas.coords(aliens[-1].id)
        if x2 >= self.largeur_jeu:  
            bords['Droite'] = True
        return bords
    
    