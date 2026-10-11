import json

from src.red_social.publicacion import Tweet
from src.red_social.red import RedSocial

def test_timeline_solo_tiene_publicaciones_de_los_seguidos(red):
   ana, luis, marta = red["@ana"], red["@luis"], red["@marta"]
   primero = red.publicar(Tweet(ana, "Primer tweet de Ana"))
   red.publicar(Tweet(marta, "Tweet de Marta"))
   segundo = red.publicar(Tweet(ana, "Segundo tweet de Ana"))
   
   assert red.timeline(luis) == [segundo, primero]
   assert red.timeline(ana) == []

def  test_desde_json_construye_usuarios_y_seguimientos(mocker):
    datos = {
        "usuarios":[
            {"nombre": "Ana", "alias": "@ana"},
            {"nombre": "Luis", "alias": "@luis"},
        ],
        "seguimientos":[["@luis", "@ana"]],
    }
    
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data=json.dumps(datos)))

    red = RedSocial.desde_json("ruta/falsa.json")

    mock_open.assert_called_once_with("ruta/falsa.json", encoding="utf-8")
    assert len(red) == 2
    assert red["@luis"].sigue_a(red["@ana"])
    assert not red["@ana"].sigue_a(red["@luis"])