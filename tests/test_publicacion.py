
import pytest
from src.red_social.publicacion import Publicacion,Tweet,Retweet

@pytest.mark.parametrize("texto_invalido",
                         [
                             "",
                             " ",
                             "a"*281
                         ])




def test_texto_invalido_lanza_error(ana, texto_invalido):

    with pytest.raises(ValueError):
        Tweet(ana,texto_invalido)
    
    
@pytest.mark.parametrize("texto, hashtags_extraidos",
                         [
                             (" ",[]),
                             ("Hola #Python #PYTEST",['#python', '#pytest']),
                             ("#python y otra vez #python",['#python']),
                             ("Me gusta #python, y mucho #pytest!",['#python', '#pytest'])
                         ])


def test_extraer_hashtags(texto, hashtags_extraidos):
    resultado = Publicacion.extraer_hashtags(texto)
    assert resultado == hashtags_extraidos


def test_retweet_comparte_el_texto_del_original(luis, tweet):
    retweet = Retweet(autor=luis,tweet_original=tweet)
    assert retweet.tweet_original is tweet
    assert retweet.texto == tweet.texto
    assert retweet.hashtags == tweet.hashtags
    assert retweet.autor is luis
    
    