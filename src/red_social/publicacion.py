from abc import ABC, abstractmethod

from Proyecto_programacion_avanzada.red_social.src.red_social.usuario import usuario


class Publicacion(ABC):
    
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
    
    
    @abstractmethod
    def __str__(self):
        pass
    
    
    
class Tweet(Publicacion):
    
    def __init__(self, autor: usuario, texto: str):
        super().__init__(autor, texto)


    def __str__(self):
        return f"Tweet de {self.autor.alias}: {self.texto}"


class Respuesta(Publicacion):
    
    def __init__(self, autor: usuario, texto: str, tweet_original: Tweet):
        super().__init__(autor, texto)
        self.tweet_original = tweet_original


    def __str__(self):
        return f"Respuesta de {self.autor.alias} al tweet de {self.tweet_original.autor.alias}: {self.texto}"
    

class Retweet(Publicacion):
    
    def __init__(self, autor: usuario, tweet_original: Tweet):
        super().__init__(autor, tweet_original.texto)
        self.tweet_original = tweet_original
    
        
    def __str__(self):
        return f"Retweet de {self.autor.alias} del tweet de {self.tweet_original.autor.alias}: {self.texto}"
    


    
    