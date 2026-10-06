from abc import ABC

from Proyecto_programacion_avanzada.red_social.src.red_social.usuario import usuario


class publicacion (ABC):
    
    def __init__(self, autor: usuario, texto: str):
        self.autor = autor
        self.texto = texto
        self.me_gusta = 0
        LIMITE_CARACTERES = 280

        if texto is None or len(texto) == 0 or len(texto) > LIMITE_CARACTERES:
            raise ValueError("El texto de la publicación no puede estar vacío.")
        
        
    def dar_me_gusta(self):
        self.me_gusta += 1
        return True
    
    
    @property
    def hashtags(self):
        return self.extraer_hashtags(self.texto)
    
    
    @staticmethod
    def extraer_hashtags(texto: str):
        palabras = texto.split()
        hashtags = [palabra for palabra in palabras if palabra.startswith('#')]
        return hashtags