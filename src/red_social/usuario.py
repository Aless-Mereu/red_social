class Usuario:
    
    def __init__(self, nombre: str, alias: str):
        self.nombre = nombre
        if not alias.startswith('@'):
            alias = '@' + alias
        self.alias = alias
        self.seguidos = []
        

    def seguir(self, otro_usuario):
        if otro_usuario in self.seguidos or otro_usuario == self:
            raise ValueError("No se puede seguir a este usuario.")
        
        self.seguidos.append(otro_usuario)
        return True 
    
    
    def sigue_a(self, otro_usuario) -> bool:
        return otro_usuario in self.seguidos

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "alias": self.alias
        }
        
        
    @property
    def numero_seguidos(self):
        return len(self.seguidos)
    
    @classmethod
    def desde_dict (cls, datos):
        return cls(
            nombre=datos["nombre"],
            alias=datos["alias"],
            
        )
        

    def __str__(self):
        return f"{self.nombre} ({self.alias})"
    
    
    def __eq__(self, otro):
        if not isinstance(otro, Usuario):
            return False
        return self.alias == otro.alias
    
