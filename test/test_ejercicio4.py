from src.ejercicio4  import frutas_en_comunes, frutas_en



frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"} 

def test_frutas_en_comunes():
    assert frutas_en_comunes(frutas1,frutas2) == {'manzana', 'pera', 'uva'}
    
def test_frutas_En():
    assert frutas_en(frutas1,frutas2) ==  {'plátano', 'naranja'}