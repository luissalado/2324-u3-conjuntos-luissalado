from src.ejercicio5 import interseccion


numeros1={2, 4, 6, 8, 10}
numeros2={9, 3, 6}
def test_interseccion():
    assert interseccion(numeros1,numeros2) == {6}