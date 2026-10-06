from .usuario import Usuario
from .publicacion import Publicacion
from collections import Counter

class RedSocial:
    
    def __init__(self):
        self.usuarios = {}
        self.publicaciones = []
        
        
    def aniadir_usuario(self, usuario: Usuario):
        if usuario.alias in self.usuarios:
            raise ValueError("El alias ya está registrado.")
        self.usuarios[usuario.alias] = usuario
        
        
    def registrar(self, nombre:str, alias:str):
        nuevo_usuario = Usuario(nombre, alias, [])
        self.aniadir_usuario(nuevo_usuario)
        
        
    def publicar(self, publicacion: Publicacion):
        self.publicaciones.append(publicacion)
        
    
    def timeline(self, usuario: Usuario):
        timeline = []
        for publicacion in self.publicaciones:
            if publicacion.autor == usuario or usuario.sigue_a_otro(publicacion.autor):
                timeline.append(publicacion)
        return timeline
    
    
    def tendencias(tweet, n=3):
        return Counter (Publicacion.hashtags).most_common(n)
    
    
    def mostrar_timeline(alias):
        pass
    
    
    def desde_json()
        
        