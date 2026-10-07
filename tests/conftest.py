import pytest

from src.red_social.usuario import Usuario
from src.red_social.publicacion import Tweet
from src.red_social.red import RedSocial 

@pytest.fixture
def ana():
    return Usuario("Ana","@ana")

@pytest.fixture
def luis():
    return Usuario("Luis" , "@luis")

@pytest.fixture
def tweet():
    return Tweet (ana, "Hola a todos #python #pytest")

@pytest.fixture
def red():
    red_social = RedSocial()
    
    red_social.registrar("Ana","@ana")
    red_social.registrar("Luis", "@luis")
    red_social.registrar("Marta", "@marta")
    return red_social
    
   
     
