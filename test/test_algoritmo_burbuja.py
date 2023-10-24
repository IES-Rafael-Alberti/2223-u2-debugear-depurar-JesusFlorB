# En un archivo llamado test_algoritmo_burbuja.py

from src.algoritmo_burbuja import algoritmo_burbuja

def test_algoritmo_burbuja():
    #Prueba con una lista desordenada
    arr1 = [8, 3, 1, 19, 14]
    algoritmo_burbuja(arr1)
    assert arr1 == [1, 3, 8, 14, 19]

def test_algoritmo_burbuja_2():
    #Prueba con una lista ya ordenada
    arr2 = [1, 3, 8, 14, 19]
    algoritmo_burbuja(arr2)
    assert arr2 == [1, 3, 8, 14, 19]

def test_algoritmo_burbuja_3():
    #Prueba con una lista vacia
    arr3 = []
    algoritmo_burbuja(arr3)
    assert arr3 == []

def test_algoritmo_burbuja_4():
    #Prueba con una lista de un solo elemento
    arr4 = [5]
    algoritmo_burbuja(arr4)
    assert arr4 == [5]

def test_algoritmo_burbuja_5():
    #Prueba con una lista de dos elementos desordenados
    arr5 = [7, 3]
    algoritmo_burbuja(arr5)
    assert arr5 == [3, 7]

def test_algoritmo_burbuja_6():
    #Prueba con una lista de dos elementos ya ordenados
    arr6 = [2, 8]
    algoritmo_burbuja(arr6)
    assert arr6 == [2, 8]