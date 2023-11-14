'''

Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.

'''

def creamos_conjunto():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    set_frutas1 = set()
    set_frutas2 = set()
    for e in frutas1:
        set_frutas1.add(e)
        
    for i in frutas2:
        set_frutas2.add(i)
        
    return set_frutas1, set_frutas2



def frutas_en_comunes(frutas1,frutas2):
    
    frutas_comunes = set()
    
    comunes = frutas1 & frutas2 
    for fruta in comunes:
        frutas_comunes.add(fruta)
        
    return frutas_comunes

def frutas_en(frutas1,frutas2):
    
    frutas_solo_en_ = frutas1 - frutas2
    return frutas_solo_en_

if __name__ == "__main__":
    
    frutas = creamos_conjunto()
    frutas1 = frutas[0]
    frutas2 = frutas[1]
    
    comunes = frutas_en_comunes(frutas1,frutas2)
    no_comunes_1 = frutas_en(frutas1,frutas2)
    no_comunes_2 = frutas_en(frutas2,frutas1)
    
    print('Las frutas comunes son:\n', comunes)
    print('Las frutas no comunes que estan en el 1 y no en el dos sin:\n', no_comunes_1)
    print('Las frutas no comunes que estan en el 1 y no en el dos sin:\n', no_comunes_2)
    
        
        
    





