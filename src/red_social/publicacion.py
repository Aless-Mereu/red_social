from abc import ABC, abstractmethod

from.usuario import Usuario

LIMITE_CARACTERES = 280
class Publicacion(ABC):
    
    def __init__(self, autor: Usuario, texto: str):
        self.autor = autor
        self.texto = texto
        self.me_gusta = 0
        

        if texto is None or len(texto.strip()) == 0 or len(texto) > LIMITE_CARACTERES:
            raise ValueError("El texto de la publicación no puede estar vacío.")
        
        
    def dar_me_gusta(self):
        self.me_gusta += 1
        return True
    
    
    @property
    def hashtags(self):
        return self.extraer_hashtags(self.texto)
    
    
    @staticmethod
    def extraer_hashtags(texto: str):
        hashtags = []
        for palabra in texto.split():
           palabra = palabra.lower().rstrip(",.;:!?¡¿")
           if palabra.startswith('#') and len(palabra) > 1 and palabra not in hashtags:
               hashtags.append(palabra)
        return hashtags
    
    
    @abstractmethod
    def __str__(self):
        pass
    
    
    
class Tweet(Publicacion):
    
    def __init__(self, autor: Usuario, texto: str):
        super().__init__(autor, texto)


    def __str__(self):
        return f"{self.autor.alias}: {self.texto}"


class Respuesta(Publicacion):
    
    def __init__(self, autor: Usuario, texto: str, original: Tweet):
        super().__init__(autor, texto)
        self.original = original


    def __str__(self):
        return f"{self.autor.alias} {self.original.autor.alias}: {self.texto}"
    

class Retweet(Publicacion):
    
    def __init__(self, autor: Usuario, tweet_original: Tweet):
        super().__init__(autor, tweet_original.texto)
        self.tweet_original = tweet_original
    
        
    def __str__(self):
        return f"{self.autor.alias} {self.original}"
    


    
    