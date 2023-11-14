from src.ejercicio2 import solicita,sin_repeticion,comunes,con_repeticion,repeticon_primaria_secundaria



conj1 = {'jose','pepe','mario'}
conj2 = {'jose','maria','javi','mario'}

def test_sin_repeticion():
    assert sin_repeticion(conj1,conj2) == {'jose','maria','javi','mario','pepe'}
    
    
def test_con_repeticion():
    assert con_repeticion(conj1,conj2) == {'jose','mario'}
    
def test_comunes():
    assert comunes(conj1,conj2) == False