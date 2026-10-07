from .usuario import Usuario
from .publicacion import Publicacion
from collections import Counter
import json


class RedSocial:
    
    def __init__(self):
        self.usuarios = {}
        self.publicaciones = []
        
        
    def anadir(self, usuario: Usuario):
        if usuario.alias in self.usuarios:
            raise ValueError("El alias ya está registrado.")
        self.usuarios[usuario.alias] = usuario
        return usuario
        
        
    def registrar(self, nombre:str, alias:str):
        return self.anadir(Usuario(nombre, alias))
        
        
    def publicar(self, publicacion: Publicacion):
        self.publicaciones.append(publicacion)
        return publicacion
        
    
    def timeline(self, usuario: Usuario):
       return [p for p in reversed(self.publicaciones) if usuario.sigue_a(p.autor)]
    
    
    def tendencias(self, n=3):
        contador = Counter()
        for publicacion in self.publicaciones:
            contador.update(publicacion.hashtags)
        return contador.most_common(n)
    
    
    def mostrar_timeline(self, alias):
        usuario = self[alias]
        print(f'\nTimeline de {usuario}:')
        for publicacion in self.timeline(usuario):
            print(f'{publicacion} {publicacion.me_gusta}')
    
    @classmethod
    def desde_json(cls, ruta):
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
            
        red = cls()
        for datos_usuario in datos['usuarios']:
            red.anadir(Usuario.desde_dict(datos_usuario))
            
        for quien_sigue, a_quien in datos["seguimientos"]:
            red[quien_sigue].seguir(red[a_quien])
            
        return red
            
    
    
    def __len__(self):
        return len(self.usuarios)
    
    
    def __iter__(self):
        return iter(sorted(self.usuarios.values(), key=lambda j: j.alias))
    
    
    def __contains__(self, alias):
        return alias in self.usuarios
    
    
    def __getitem__(self, alias):
        return self.usuarios[alias]
