import pygame
import os
from enemies.Enemy import Enemy


class Gboss(Enemy):
    def __init__(self, x: float, y: float, screen_size: tuple) -> None:
        super().__init__(x, y, screen_size)
        """Sous-classe de l'ennemi boss slime vert
        - x: nombre réel correspondant à la position x de la tour
        - y: nombre réel correspondant à la position y de la tour
        - screen_size: tuple contenant la largeur et la hauteur de la fenêtre"""
        self.width = screen_size[1]/9
        self.height = screen_size[1]/9
        self.max_speed = 6
        self.speed = 6
        self.image_path = os.path.join("assets", "enemies", "boss_green.png")
        self.image = pygame.image.tostring(pygame.transform.scale(
            pygame.image.load(self.image_path), (self.width, self.height)), "RGBA")
        self.health = 500
        self.max_health = 500
        self.bouclier = 250
        self.max_bouclier = 250
        self.resistance = {
            "Magic": 4,
            "Physical": 12,
        }
        self.max_resistance_magic = self.resistance["Magic"]
        self.max_resistance_physic = self.resistance["Physical"]
        self.damage = 100
        self.money_value = 100
        self.type = "Boss"

    def bar_switch(self):
        """Méthode pour changer les résistances de l'ennemi lorsque son bouclier tombe en dessous de 0"""
        if self.bouclier <= 0:
            self.resistance = {
                "Magic": 4,
                "Physical": 4,
            }

    def Bresistance(self):
        """Méthode pour retourner si l'ennemi possède encore du bouclier"""
        return self.bouclier > 0
